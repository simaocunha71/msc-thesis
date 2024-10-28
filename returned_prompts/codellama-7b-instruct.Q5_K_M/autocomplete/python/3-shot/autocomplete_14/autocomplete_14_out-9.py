
      assets = jsonpickle.decode(rv.data)
    self.assertIsNotNone(assets, 'No results after deserialization')
    self.assertIsInstance(assets, dict, 'The result is not a dictionary as expected')
    self.assertEqual(len(assets), 2, 'The length of the dictionary is different than expected')
    self.assertEqual(len(assets['types']), 1, 'There should be one type in the dictionary')
    self.assertEqual(len(assets['assets']), 1, 'There should be one asset in the dictionary')
    self.assertEqual(assets['types'][0]['type_name'], 'asset_type', 'The type name is not correct')
    self.assertEqual(assets['assets'][0]['type_name'], 'asset_type', 'The asset type name is not correct')
    self.assertEqual(assets['assets'][0]['asset_name'], 'asset', 'The asset name is not correct')

  def test_types_get_type_id(self):
    method = 'test_types_get_type_id'
    rv = self.app.get('/api/assets/types?session_id=test')
    if (sys.version_info > (3,)):
      assets = jsonpickle.decode(rv.data.decode('utf-8'))
    else:
      assets = jsonpickle.decode(rv.data)
    self.assertIsNotNone(assets, 'No results after deserialization')
    self.assertIsInstance(assets, dict, 'The result is not a dictionary as expected')
    self.assertEqual(len(assets), 2, 'The length of the dictionary is different than expected')
    self.assertEqual(len(assets['types']), 1, 'There should be one type in the dictionary')
    self.assertEqual(len(assets['assets']), 1, 'There should be one asset in the dictionary')
    self.assertEqual(assets['types'][0]['type_name'], 'asset_type', 'The type name is not correct')
    self.assertEqual(assets['assets'][0]['type_name'], 'asset_type', 'The asset type name is