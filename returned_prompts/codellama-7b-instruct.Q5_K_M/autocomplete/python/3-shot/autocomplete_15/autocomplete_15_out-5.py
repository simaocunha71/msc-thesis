
    self.assertIsNotNone(postResponse, 'No results after deserialization')
    self.assertIsInstance(postResponse, dict, 'The response is not a valid JSON dictionary')

    message = jsonpickle.decode(rv.data)
    self.assertIsNotNone(message, 'No results after deserialization')
    self.assertIsInstance(message, dict, 'The response is not a valid JSON dictionary')

    self.assertEquals(rv.status_code, 200, 'Status code is not 200')

    self.logger.info('[%s] Response data: %s', method, message)

    self.logger.info('[%s] Asset Type created successfully', method)

    return message

  def prepare_new_asset_type(self):
    """
    Create a new asset type object for the test
    """
    new_asset_type = {}

    new_asset_type['name'] = 'Test Asset Type'
    new_asset_type['description'] = 'Test asset type description'
    new_asset_type['schema'] = {}
    new_asset_type['schema']['schema_type'] = 'Asset'
    new_asset_type['schema']['properties'] = {}
    new_asset_type['schema']['properties']['name'] = {}
    new_asset_type['schema']['properties']['name']['type'] = 'string'
    new_asset_type['schema']['properties']['name']['description'] = 'The name of the asset'
    new_asset_type['schema']['properties']['name']['required'] = 'true'

    return new_asset_type

  def test_create_asset_type(self):
    """
    Test case for create_asset_type

    Create asset type
    """
    self.logger.info('[%s] Create Asset Type', __name__)
    asset_type = self.prepare_new_asset_type()
    url = '/asset-types'
    method = 'test_create_asset_type'
    self.logger.info('[%s] URL: %s', method, url)
    self.logger.info('[%s