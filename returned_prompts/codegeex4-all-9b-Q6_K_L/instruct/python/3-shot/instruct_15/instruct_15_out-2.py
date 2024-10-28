    
    Example:

    >>> send_request('http://example.com', 'POST', 'json_payload', 'DELETE', 'param=value')
    {'key': 'value', 'other_key': 'other_value'}
    
    >>> send_request('http://example.com', 'POST', 'json_payload', 'DELETE', 'param=value')
    {}
    
    >>> send_request('http://example.com', 'POST', 'json_payload', 'DELETE', 'param=value')
    Traceback (most recent call last):
        ...
    requests.exceptions.RequestException: HTTP request failed
    >>> send_request('http://example.com', 'POST', 'json_payload', 'DELETE', 'param=value')
    Traceback (most recent call last):
        ...
    ValueError: Invalid JSON response

    # Write your implementation below this line

```python
import json
import requests

def send_request(url, method, payload, delete_method, delete_param):
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        response_dict = response.json()
        
        if 'key' in response_dict and response_dict['key'] == 'value':
            delete_response = requests.delete(url, params={delete_param})
            delete_response.raise_for_status()
            return response_dict
        else:
            return {}
    except requests.exceptions.RequestException as e:
        raise e
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON response")
```