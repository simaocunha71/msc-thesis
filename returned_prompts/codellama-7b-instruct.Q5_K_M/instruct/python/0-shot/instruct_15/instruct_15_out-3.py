
    import requests
    import json

    def send_and_delete():
        # Send a POST request to the server
        url = "http://www.example.com/post"
        data = {"key1": "value1", "key2": "value2"}
        response = requests.post(url, json=data)

        # Check if the response contains the expected key and value
        if "key3" in response.json() and response.json()["key3"] == "value3":
            # Send a DELETE request to the server
            url = "http://www.example.com/delete?key1=value1"
            response = requests.delete(url)
            return response.json()
        else:
            return None
