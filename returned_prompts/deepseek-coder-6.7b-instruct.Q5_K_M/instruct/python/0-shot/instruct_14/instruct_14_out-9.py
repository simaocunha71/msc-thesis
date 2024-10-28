import requests
import json
import logging

def test_api_endpoints(base_url, asset_types):
    logging.basicConfig(filename='api_test.log', level=logging.INFO)

    for asset_type in asset_types:
        url = base_url + '/asset_types/' + asset_type

        # Test retrieving an asset type
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            logging.info(f'Successfully retrieved asset type {asset_type}: {data}')
        else:
            logging.error(f'Failed to retrieve asset type {asset_type} with status code {response.status_code}')

        # Test deleting an asset type
        response = requests.delete(url)
        if response.status_code == 200:
            logging.info(f'Successfully deleted asset type {asset_type}')
        else:
            logging.error(f'Failed to delete asset type {asset_type} with status code {response.status_code}')

