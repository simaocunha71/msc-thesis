    import requests
    import json
    def send_requests(url, json_payload, delete_query):
        response = requests.post(url, json=json_payload)
        response = response.json()
        if 'key' in response and response['key'] == 'value':
            print('Response contains key and value.')
        else:
            print('Response does not contain key and value.')
        response = requests.delete(url, params={'query': delete_query})
        response = response.json()
        return response
    send_requests('http://example.com/api', {'key': 'value'}, 'delete_query') 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
    {'key': 'value'} 
    {'message': 'Record deleted'} 
    {'query': 'delete_query'} 
   