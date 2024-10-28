    import requests
    import json
    import logging

    def test_api_endpoints(base_url, asset_types):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)

        for asset_type in asset_types:
            # Retrieve asset type
            retrieve_url = f"{base_url}/assets/{asset_type}"
            response = requests.get(retrieve_url)

            if response.status_code == 200:
                logger.info(f"Successfully retrieved asset type {asset_type}")
                data = response.json()
                logger.info(f"Retrieved data: {data}")
            else:
                logger.error(f"Failed to retrieve asset type {asset_type}. Status code: {response.status_code}")

            # Delete asset type
            delete_url = f"{base_url}/assets/{asset_type}"
            response = requests.delete(delete_url)

            if response.status_code == 200:
                logger.info(f"Successfully deleted asset type {asset_type}")
            else:
                logger.error(f"Failed to delete asset type {asset_type}. Status code: {response.status_code}")

