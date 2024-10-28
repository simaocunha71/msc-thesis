def send_request(url, payload, key, value):
    import requests
    import json
    import decimal

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=payload)
    decoded_response = json.loads(response.text)

    if key in decoded_response.keys() and decoded_response[key] == value:
        return decoded_response
    else:
        return None

