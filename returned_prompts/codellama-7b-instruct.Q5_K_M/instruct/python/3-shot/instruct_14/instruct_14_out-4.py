def test_api_asset_types(api_url, token, asset_types):
    logger = logging.getLogger(__name__)

    # Get all asset types.
    response = requests.get(api_url + '/v1/asset_types', headers={'Authorization': 'Bearer ' + token})
    if response.status_code != 200:
        logger.error('GET /v1/asset_types returned status code %s', response.status_code)
        return False
    else:
        asset_types_response = response.json()
        logger.info('GET /v1/asset_types returned %s asset types', len(asset_types_response))

    # Delete asset types.
    for asset_type in asset_types:
        logger.info('Deleting asset type %s', asset_type)
        response = requests.delete(api_url + '/v1/asset_types/' + asset_type, headers={'Authorization': 'Bearer ' + token})
        if response.status_code != 204:
            logger.error('DELETE /v1/asset_types/%s returned status code %s', asset_type, response.status_code)
            return False

    # Get all asset types again.
    response = requests.get(api_url + '/v1/asset_types', headers={'Authorization': 'Bearer ' + token})
    if response.status_code != 200:
        logger.error('GET /v1/asset_types returned status code %s', response.status_code)
        return False
    else:
        asset_types_response = response.json()
        logger.info('GET /v1/asset_types returned %s asset types', len(asset_types_response))

    # Compare asset types.
    if len(asset_types_response) != 0:
        logger.error('Asset types not deleted')
        return False

    return True

