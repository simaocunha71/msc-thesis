
from hashlib import md5

def string_to_md5(text):
    hash_object = md5(text.encode())
    if len(text) == 0:
        return None
    return hash_object.hexdigest()

# Unit Tests
from __future__ import print_function
from __future__ import division
import unittest

class TestStringToMD5(unittest.TestCase):

    def test_string_to_md5(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertEqual(string_to_md5(''), None)

if __name__ == '__main__':
    unittest.main()































```
import hashlib

def string_to_md5(text):
    if len(text) == 0:
        return None
    return hashlib.md5(text.encode()).hexdigest()
```