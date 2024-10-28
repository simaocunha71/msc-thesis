    import requests
    import json

    def send_requests(url, key, value):
        # Send POST request with JSON payload
        response = requests.post(url, json={'param': 'value'})
        response.raise_for_status()

        # Send DELETE request with query parameter
        delete_response = requests.delete(url, params={'param': value})
        delete_response.raise_for_status()

        # Decode response and check for key-value pair
        response_json = response.json()
        if key in response_json and response_json[key] == value:
            return response_json
        else:
            return None
