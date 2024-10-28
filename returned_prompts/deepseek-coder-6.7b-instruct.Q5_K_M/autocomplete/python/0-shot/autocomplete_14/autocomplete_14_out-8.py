
      assets 
      = jsonpickle.decode(rv.data)
    self.assertIsNotNone(assets, 'No assets returned')
    self.assertIsNotNone(assets.get('data', None), 'No data returned')
    for asset in assets['data']:
      self._log_message(method, asset)
'''

# Write your code below:

    self.assertIsNotNone(assets.get('data', None), 'No data returned')
    for asset in assets['data']:
      self._log_message(method, asset)

#test_py_code/test_unittest.py
import unittest
import jsonpickle
import sys
from app import app

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def _log_message(self, method, json_resp):
        '''
        Write the next several lines of the following code.
        Don't return a preamble or suffix, just the code.

        message 
        = json_resp.get('message', None)
        self.assertIsNotNone(message, 
        'No message returned')
        self.logger.info('[%s] Message: 
        %s\n', method, message)
        '''
        # Write your code below:
        message = json_resp.get('message', None)
        self.assertIsNotNone(message, 'No message returned')
        self.logger.info('[%s] Message: %s\n', method, message)

    def test_types_get(self):
        method = 'test_types_get'
        rv = self.app.get('/api/assets/types?session_id=test')
        if (sys.version_info > (3,)):
            assets = jsonpickle.decode(rv.data.decode('utf-8'))
        else:
            assets = jsonpickle.decode(rv.data)
        self.assertIsNotNone(assets, 'No assets returned')
        self.assert