      assets = jsonpickle.decode(rv.data)
    self.assertIsNotNone(assets, 'No results after deserialization')
    self.assertIsInstance(assets, dict, 'Assets not a dictionary')
    if 'types' in assets:
      types = assets.get('types', None)
      self.assertIsInstance(types, list, 'Types not a list as expected')

