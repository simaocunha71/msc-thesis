      assets 
      = jsonpickle.decode(rv.data)
    self.assertIsNotNone(assets, 'No assets returned')
    self.assertIn('asset_types', assets, 'No asset types returned')
    self.assertEqual(len(assets['asset_types']), 4, 'Wrong number of asset types returned')

