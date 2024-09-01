import unittest
from unittest.mock import patch


class TestWeatherFunction(unittest.TestCase):

    @patch('yourapp.weather.requests.get')
    def test_get_weather_data_success(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: [{'lat': 48.8588443, 'lon': 2.2943506}]),
            unittest.mock.Mock(status_code=200, json=lambda: {'current': {'temp': 15}})
        ]

        response = get_weather_data("Paris")
        self.assertIsNotNone(response)
        self.assertIn('current', response)
        self.assertEqual(response['current']['temp'], 15)

    @patch('yourapp.weather.requests.get')
    def test_get_weather_data_geocoding_failure(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: []),
        ]

        response = get_weather_data("UnknownCity")
        self.assertIsNone(response)

    @patch('yourapp.weather.requests.get')
    def test_get_weather_data_weather_failure(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: [{'lat': 48.8588443, 'lon': 2.2943506}]),
            unittest.mock.Mock(status_code=404, json=lambda: {'error': 'not found'})
        ]

        response = get_weather_data("Paris")
        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
