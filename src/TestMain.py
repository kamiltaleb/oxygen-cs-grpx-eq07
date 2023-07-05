import unittest
import logging
from unittest.mock import MagicMock, patch
from signalrcore.hub_connection_builder import HubConnectionBuilder
from src.main import Main

class TestMain(unittest.TestCase):

    @patch('src.main.HubConnectionBuilder')
    @patch('src.main.requests')
    def test_setSensorHub(self, mock_requests, mock_hub_builder):
        # Mocking the requests.get
        mock_requests.get.return_value = MagicMock(text='{"success": true, "message": "Action sent."}')

        hub_builder_mock = MagicMock()
        mock_hub_builder.return_value = hub_builder_mock

        main = Main()
        main.setSensorHub()

        # Verify that the HubConnectionBuilder methods were called with the expected arguments
        hub_builder_mock.with_url.assert_called_with(f"{main.HOST}/SensorHub?token={main.TOKEN}")
    
    

