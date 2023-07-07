import unittest
from unittest.mock import MagicMock, patch
from signalrcore.hub_connection_builder import HubConnectionBuilder
from src.main import Main
import os


class test_main(unittest.TestCase):
    @patch("src.main.HubConnectionBuilder")
    @patch("src.main.requests")
    def test_if_var_enviro_exist(self, mock_requests, mock_hub_builder):
        self.assertIsNotNone(os.environ.get("HOST"), "HOST VARIABLE IS MISSING")
        self.assertIsNotNone(os.environ.get("TOKEN"), "TOKEN VARIABLE IS MISSING")
        self.assertIsNotNone(os.environ.get("TICKETS"), "TICKETS VARIABLE IS MISSING")
        self.assertIsNotNone(os.environ.get("T_MAX"), "T_MAX VARIABLE IS MISSING")
        self.assertIsNotNone(os.environ.get("T_MIN"), "T_MIN VARIABLE IS MISSING")

    def test_var_enviro_default_value(self):
        if "TICKETS" in os.environ:
            del os.environ["TICKETS"]
        tickets = os.environ.get("TICKETS", default="1")
        self.assertEqual(tickets, "1")
        if "T_MAX" in os.environ:
            del os.environ["T_MAX"]
        t_max = os.environ.get("T_MAX", default="25")
        self.assertEqual(t_max, "25")
        if "T_MIN" in os.environ:
            del os.environ["T_MIN"]
        t_min = os.environ.get("T_MIN", default="17")
        self.assertEqual(t_min, "17")

    def test_temp_in_valid_borns(self):
        tmax = os.environ.get("T_MAX")
        tmin = os.environ.get("T_MIN")
        self.assertGreater(int(tmin), 10, "TEMP TOO COLD, SOMETHING WRONG")
        self.assertLess(int(tmax), 100, "TEMP TOO HOT, SOMETHING WRONG")
