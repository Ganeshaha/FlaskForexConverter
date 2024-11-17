from unittest import TestCase
from app import app
import json

class ConverterTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
    
    def test_homepage(self):
        with self.client as client:
            response = client.get('/')

            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('form method="POST" id="converter-form', html)
            
    def test_converter(self):
        with self.client as client:
            response = client.post('/submit', data = json.dumps({
            "fromValue": "USD",
            "toValue": "EUR",
            "amountValue": "100"
            }))
            response_parsed = response.json

            response_string = response.get_data(as_text=True)
            self.assertIn('result', response_string)
            
            self.assertIn('"success": true', response_string)
           
            for key in response_parsed:{ 
            print(key,":", response_parsed[key]) }
            
            self.assertEqual(response_parsed["query"]["from"], "USD")
            self.assertEqual(response_parsed["query"]["to"], "EUR")
            self.assertEqual(response_parsed["query"]["amount"], 100)
            
            result_reasonable = True if response_parsed["result"]<100 and response_parsed["result"] >90 else False
            
            self.assertTrue(result_reasonable)
            # could also convert from USD to USD to test
      
            
