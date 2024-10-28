    import logging
    import requests
    from requests.exceptions import HTTPError
    import json
    import time

    def test_asset_type_endpoints(logger, asset_type_id, url, token):
        try:
            # Get asset type
            response = requests.get(f"{url}/asset-types/{asset_type_id}", headers={'Authorization': f'Bearer {token}'})
            response.raise_for_status()
            asset_type = response.json()

            # Delete asset type
            response = requests.delete(f"{url}/asset-types/{asset_type_id}", headers={'Authorization': f'Bearer {token}'})
            response.raise_for_status()
            logger.info(f"Successfully deleted asset type {asset_type_id}")
        except HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
        finally:
            time.sleep(1)  # Add a delay to avoid rate limiting

