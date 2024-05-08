import unittest
from unittest.mock import patch

from main import app


class GetAvgPricesAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('main.get_avg_prices')
    def test_get_avg_prices_api(self, mock_get_avg_prices):
        mock_data = {
            "2016-01-01": 1154.67,
            "2016-01-02": 1154.67
        }
        mock_get_avg_prices.return_value = mock_data
        query_string = {
            'origin_slug': 'china',
            'destination_slug': 'japan',
            'start_date': '2016-01-01',
            'end_date': '2017-01-01'
        }
        response = self.app.get('/get_avg_prices', query_string=query_string)

        self.assertEqual(response.status_code, 200)

        json_data = response.get_json()
        expected_data = {
            "2016-01-01": 1154.67,
            "2016-01-02": 1154.67
        }
        self.assertEqual(json_data, expected_data)

        mock_get_avg_prices.assert_called_with(query_string)


if __name__ == '__main__':
    unittest.main()