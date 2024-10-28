    import requests
    import json
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    def test_asset_types(api_url):
        try:
            response = requests.get(api_url + '/asset_types')
            response.raise_for_status()
            asset_types = json.loads(response.content)
            logger.info(f'Asset types retrieved: {len(asset_types)}')

            for asset_type in asset_types:
                asset_type_id = asset_type['id']
                logger.info(f'Deleting asset type {asset_type_id}...')
                response = requests.delete(api_url + f'/asset_types/{asset_type_id}')
                response.raise_for_status()
                logger.info(f'Asset type {asset_type_id} deleted')

        except requests.exceptions.RequestException as e:
            logger.error(f'Error testing API: {e}')
        except json.JSONDecodeError as e:
            logger.error(f'Error parsing JSON: {e}')
        except Exception as e:
            logger.error(f'Error: {e}')
