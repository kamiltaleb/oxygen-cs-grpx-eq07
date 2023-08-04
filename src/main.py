from signalrcore.hub_connection_builder import HubConnectionBuilder
import logging
import requests
import json
import time
from dotenv import load_dotenv
import os
import mysql.connector 
from mysql.connector import Error
import psycopg2

load_dotenv()


class Main:
    def __init__(self):
        self.last_temperature = None
        self._hub_connection = None
        self.HOST = os.getenv("HOST")  # Setup your host here
        self.TOKEN = os.getenv("TOKEN", default='fMupq1cdfE')  # Setup your token here
        if not self.TOKEN:
            raise ValueError("The TOKEN environment variable is not set.")
        self.TICKETS = os.environ.get("TICKETS", default=1)  # Setup your tickets here
        self.T_MAX = os.environ.get(
            "T_MAX", default=25
        )  # Setup your max temperature here
        self.T_MIN = os.environ.get("T_MIN", default=17)
        self.DATABASE = self.connect_to_database()

    def connect_to_database(self):
        try:
            # Replace these variables with your actual database credentials
            host = os.getenv("DATABASE_HOST")
            database_name = os.getenv("DATABASE_NAME")
            user = os.getenv("DATABASE_USER")
            password = os.getenv("DATABASE_PWD")

            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                host=host,
                database=database_name,
                user=user,
                password=password
            )

            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()[0]
            print("Connected to DB", db_version)

            return connection

        except Exception as e:
            # In case of an error, raise or handle it as needed
            raise e

    def __del__(self):
        if self._hub_connection != None:
            self._hub_connection.stop()

    def setup(self):
        self.setSensorHub()

    def start(self):
        self.setup()
        self._hub_connection.start()

        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def setSensorHub(self):
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.HOST}/SensorHub?token={self.TOKEN}")
            .configure_logging(logging.INFO)
            .with_automatic_reconnect(
                {
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 999,
                }
            )
            .build()
        )

        self._hub_connection.on("ReceiveSensorData", self.onSensorDataReceived)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(
            lambda data: print(f"||| An exception was thrown closed: {data.error}")
        )

    def onSensorDataReceived(self, data):
        try:
            print(data[0]["date"] + " --> " + data[0]["data"])
            date = data[0]["date"]
            dp = float(data[0]["data"])
            self.send_event_to_database(date,dp)
            self.send_temperature_to_fastapi(date, dp)
            self.analyzeDatapoint(date, dp)
        except Exception as err:
            print(err)

    def analyzeDatapoint(self, date, data):
        if float(data) >= float(self.T_MAX):
            self.sendActionToHvac(date, "TurnOnAc", self.TICKETS)
        elif float(data) <= float(self.T_MIN):
            self.sendActionToHvac(date, "TurnOnHeater", self.TICKETS)

    def sendActionToHvac(self, date, action, nbTick):
        r = requests.get(f"{self.HOST}/api/hvac/{self.TOKEN}/{action}/{nbTick}")
        details = json.loads(r.text)
        print(details)

    def send_event_to_database(self, timestamp, event):

        try:
            query = "INSERT INTO temperatures (temperature_celsius, time, message) VALUES ( %s, %s, %s);"
            cursor = self.DATABASE.cursor()

            temperature_celsius = float(event)

            # Check if the last temperature data exists and compare it with the new one
            if self.last_temperature is not None:
                if self.last_temperature > (temperature_celsius + 2):
                    message = "Activating AC"
                elif self.last_temperature < (temperature_celsius - 2):
                    message = "Activating Heater"
                else:
                    message = "Normal"
            else:
                message = "Normal"
            
            self.last_temperature = temperature_celsius


            cursor.execute(query, (temperature_celsius, timestamp, message))
            self.DATABASE.commit()
            cursor.close()
            pass
        except mysql.connector.Error as e:
            print(f"An error occurred while executing the SQL query: {e}")


if __name__ == "__main__":
    main = Main()
    main.start()
