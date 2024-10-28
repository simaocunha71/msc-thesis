```python
import requests
import json

def send_request_and_delete(server_url, json_payload, query_param):
    response = requests.post(server_url, json=json_payload)

    if response.status_code == 200:
        decoded_response = json.loads(response.text)
        if 'specific_key' in decoded_response and decoded_response['specific_key'] == 'specific_value':
            return decoded_response
        else:
            delete_response = requests.delete(server_url, params={'param': query_param})
            if delete_response.status_code == 200:
                return json.loads(delete_response.text)
            else:
                return None
    else:
        return None
```