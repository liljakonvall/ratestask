import unittest
from persistence import get_avg_prices


class PersistenceIntegrationTestCases(unittest.TestCase):

    def test_region_to_region(self):
        input_params = {
            'origin_slug': 'china_main',
            'destination_slug': 'uk_main',
            'start_date': '2016-01-01',
            'end_date': '2016-01-02'
        }

        results = get_avg_prices(input_params)
        expected_result = {'2016-01-01': 1245.7, '2016-01-02': 1245.92}

        self.assertEqual(results, expected_result)

    def test_port_to_region(self):
        input_params = {
            'origin_slug': 'CNGGZ',
            'destination_slug': 'baltic_main',
            'start_date': '2016-01-01',
            'end_date': '2016-01-02'
        }

        results = get_avg_prices(input_params)
        expected_result = {'2016-01-01': 1154.67, '2016-01-02': 1154.67}

        self.assertEqual(results, expected_result)

    def test_region_to_port(self):
        input_params = {
            'origin_slug': 'china_main',
            'destination_slug': 'EETLL',
            'start_date': '2016-01-01',
            'end_date': '2016-01-02'
        }

        results = get_avg_prices(input_params)
        expected_result = {'2016-01-01': 1094.24, '2016-01-02': 1094.24}

        self.assertEqual(results, expected_result)

    def test_port_to_port(self):
        input_params = {
            'origin_slug': 'CNGGZ',
            'destination_slug': 'EETLL',
            'start_date': '2016-01-01',
            'end_date': '2016-01-02'
        }

        results = get_avg_prices(input_params)
        expected_result = {'2016-01-01': 1154.67, '2016-01-02': 1154.67}

        self.assertEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()