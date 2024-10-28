    import json
    import requests

    def send_request(url, payload):
        # Send a POST request to the server
        response = requests.post(url, json=payload)

        # Check if the response contains the specific key and value
        if 'key' in response.json() and response.json()['key'] == 'value':
            # Send a DELETE request to the server with a query parameter
            response = requests.delete(url, params={'key': 'value'})

            # Check if the response is valid
            if response.status_code == 200:
                return response.json()

