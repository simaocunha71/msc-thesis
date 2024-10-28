
    Assumptions:
    - The API endpoint is available at "http://example.com/api/asset_types"
    - The API uses standard HTTP methods: GET, POST, PUT, DELETE
    - The API expects/returns JSON data
    - The API requires authentication, which is done via a header "Authorization: Bearer <token>"
    - The API has an endpoint "http://example.com/api/asset_types/<id>" to manipulate a specific asset type
    - The API returns a unique id for each created asset type
    - The API returns a status field in its responses indicating success or failure
    - The API expects a JSON body with the new asset type data when creating a new asset type
    - The API returns an asset type data when retrieving it
    - The API expects no body when deleting an asset type
    """

    import requests
    import json
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('asset_types_api_test')

    def test_asset_types_api(token, asset_type_id, new_asset_type_data):
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }

        base_url = "http://example.com/api/asset_types"

        # Test GET on /asset_types
        try:
            response = requests.get(base_url, headers=headers)
            response.raise_for_status()
            logger.info('GET on /asset_types successful')
        except requests.HTTPError as e:
            logger.error(f'Error during GET on /asset_types: {e}')

        # Test POST on /asset_types
        try:
            response = requests.post(base_url, headers=headers, data=json.dumps(new_asset_type_data))
            response.raise_for_status()
            logger.info('POST on /asset_types successful')
        except requests.HTTPError as e:
            logger.error(f'Error during POST on /ass