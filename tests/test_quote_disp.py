import unittest
from unittest.mock import patch
from quote_disp.app import app 

class QuoteDispTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        app.testing = True

    @patch('quote_disp.app.requests.get')
    def test_get_quote_renders_correct_template_with_quote(self, mock_get):
        # Mock the response of the external request
        mock_get.return_value.text = "Mocked Quote"

        response = self.client.get('/get_quote')

        self.assertEqual(response.status_code, 200)
        # Check if the response contains the mocked quote
        self.assertIn("Mocked Quote", response.get_data(as_text=True))
        # Further checks can be added to ensure the correct template is rendered

if __name__ == '__main__':
    unittest.main()
