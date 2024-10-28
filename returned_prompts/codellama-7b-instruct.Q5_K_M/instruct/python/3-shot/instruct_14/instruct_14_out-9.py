    """
    # import libraries
    import requests
    import json
    from logging import basicConfig, getLogger

    # set up logging
    logger = getLogger(__name__)
    basicConfig(level="INFO")

    # set up API endpoint
    api_url = "http://localhost:8000/api/asset_types"

    # get list of asset types
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    logger.info(f"Retrieved {len(data)} asset types")

    # delete all asset types
    for asset_type in data:
        asset_type_url = f"{api_url}/{asset_type['id']}"
        response = requests.delete(asset_type_url)
        response.raise_for_status()
        logger.info(f"Deleted asset type {asset_type['name']}")


def test_api_endpoints_asset_types_with_standard_library_functions_and_json_serialization_deserialization_and_logging_to_logger_pretty_print(
    caplog,
):
    """
    Write a Python function that tests API endpoints for retrieving and deleting asset types, using standard library functions and JSON serialization/deserialization, and logs relevant information to a logger.

    Only return the code, don't include any other information,
    such as a preamble or suffix.
    """
    # import libraries
    import requests
    import json
    from logging import basicConfig, getLogger

    # set up logging
    logger = getLogger(__name__)
    basicConfig(level="INFO")

    # set up API endpoint
    api_url = "http://localhost:8000/api/asset_types"

    # get list of asset types
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    logger.info(f"Retrieved {len(data)} asset types")

    # delete all asset types
    for asset_type in data:
        asset_type_