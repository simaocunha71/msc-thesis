    import requests
    import json

    def send_request(url, data, key, value):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response_data = json.loads(response.text)
        
        if key in response_data and response_data[key] == value:
            return response_data

        requests.delete(url, params={'key': key, 'value': value})
        return None

