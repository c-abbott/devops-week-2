import unittest
from quote_gen.app import app

class FlaskAppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the test client once for all tests
        cls.client = app.test_client()
        app.testing = True

    def test_quote_endpoint_returns_valid_quote(self):
        response = self.client.get('/quote')
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.get_data(as_text=True), [
            "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
            "The way to get started is to quit talking and begin doing. -Walt Disney",
            "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs",
            "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
            "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey",
            "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron",
        ])

if __name__ == '__main__':
    unittest.main()