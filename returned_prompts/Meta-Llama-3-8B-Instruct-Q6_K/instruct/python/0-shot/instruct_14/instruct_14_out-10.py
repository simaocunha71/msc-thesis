    """
    import requests
    import json
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    def test_asset_types_api(endpoint_url, api_key):
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(endpoint_url, headers=headers)
        response_json = json.loads(response.text)
        logger.info(f"Retrieved asset types: {response_json}")

        if response.status_code == 200:
            asset_types = response_json
            for asset_type in asset_types:
                delete_url = f"{endpoint_url}/{asset_type['id']}"
                delete_response = requests.delete(delete_url, headers=headers)
                delete_response_json = json.loads(delete_response.text)
                logger.info(f"Deleted asset type {asset_type['name']}: {delete_response_json}")

        return response.status_code
    """



    # Example usage:
    endpoint_url = "https://api.example.com/asset-types"
    api_key = "your_api_key_here"

    status_code = test_asset_types_api(endpoint_url, api_key)
    print(f"API endpoint returned status code {status_code}")""""""

    # Example log output:
    # INFO:root:Retrieved asset types: [{'id': 1, 'name': 'Type A'}, {'id': 2, 'name': 'Type B'}]
    # INFO:root:Deleted asset type Type A: {'message': 'Asset type deleted successfully'}
    # INFO:root:Deleted asset type Type B: {'message': 'Asset type deleted successfully'}""""""

    # Example error handling:
    try:
        test_asset_types_api(endpoint_url, api_key)
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making request: {e}")
        print(f"Error making request: {e}")""""""

    # Example log output:
    # ERROR:root:Error making request: ConnectionError('Connection to https://api.example.com/asset-types refused',)""""""

    # Example additional logging configuration:
    logging.basicConfig(filename='api_test.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')""""""

    # Example log output in the log file:
    # 2022-01-01 12:00:00,000 - root - INFO - Retrieved asset types: [{'id': 1, 'name': 'Type A'}, {'id': 2