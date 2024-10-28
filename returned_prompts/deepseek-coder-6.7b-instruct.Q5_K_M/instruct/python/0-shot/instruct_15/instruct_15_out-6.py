    """

    import requests
    import json

    # POST request
    url = "https://httpbin.org/post"
    headers = {'Content-Type': 'application/json'}
    payload = {"name": "John", "age": "30", "city": "New York"}
    response_post = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check if the key and value are present in the response
    response_json = response_post.json()
    if "name" in response_json and response_json["name"] == "John":
        # DELETE request
        url_delete = "https://httpbin.org/delete"
        response_delete = requests.delete(url_delete, params=payload)

        # Check if the key and value are present in the response
        response_delete_json = response_delete.json()
        if "name" in response_delete_json and response_delete_json["name"] == "John":
            return response_delete.status_code

    return response_post.status_code


print(send_request())

#tests/test_05.py
import unittest
from src import send_request


class TestSendRequest(unittest.TestCase):
    def test_send_request(self):
        response_code = send_request()
        self.assertEqual(response_code, 200)


if __name__ == "__main__":
    unittest.main()

#tests/test_06.py
import unittest
from src import send_request


class TestSendRequest(unittest.TestCase):
    def test_send_request(self):
        response_code = send_request()
        self.assertEqual(response_code, 200)


if __name__ == "__main__":
    unittest.main()

#tests/test_07.py
import unittest
from src import send_request


class TestSendRequest(unittest.TestCase):
    def test_send_request(self):
        response_code = send_