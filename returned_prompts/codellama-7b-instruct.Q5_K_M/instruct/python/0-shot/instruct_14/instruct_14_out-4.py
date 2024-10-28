
    import json
    import requests
    import logging

    def test_endpoints(self, base_url, asset_type_ids, logger):
        session = requests.Session()

        for asset_type_id in asset_type_ids:
            url = '{}/api/asset_types/{}'.format(base_url, asset_type_id)
            logger.info('GET {}'.format(url))
            response = session.get(url)
            logger.info('status code: {}'.format(response.status_code))
            response_json = response.json()
            logger.info(json.dumps(response_json, indent=4))

            url = '{}/api/asset_types/{}/delete'.format(base_url, asset_type_id)
            logger.info('DELETE {}'.format(url))
            response = session.delete(url)
            logger.info('status code: {}'.format(response.status_code))
            response_json = response.json()
            logger.info(json.dumps(response_json, indent=4))

