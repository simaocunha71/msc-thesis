import json
import logging
import requests

def test_asset_type_api(logger):
    """
    Tests the API endpoints for retrieving and deleting asset types.
    Logs relevant information to the logger.
    """
    asset_type_url = "https://example.com/api/v1/asset_types"
    delete_url = "https://example.com/api/v1/asset_types/1"

    # Retrieve asset types
    response = requests.get(asset_type_url)
    if response.status_code == 200:
        asset_types = json.loads(response.text)
        logger.info(f"Retrieved {len(asset_types)} asset types.")
    else:
        logger.error(f"Failed to retrieve asset types. Status code: {response.status_code}")

    # Delete asset type
    response = requests.delete(delete_url)
    if response.status_code == 204:
        logger.info("Asset type deleted successfully.")
    else:
        logger.error(f"Failed to delete asset type. Status code: {response.status_code}")