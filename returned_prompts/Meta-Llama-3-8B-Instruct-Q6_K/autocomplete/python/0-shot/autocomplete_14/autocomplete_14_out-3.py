 
      assets = jsonpickle.decode(rv.data)
    self.assertIsNotNone(assets, 'No assets returned')
    self.logger.info('[%s] Assets: %s\n', method, assets)

  def test_types_post(self):
    method = 'test_types_post'
    data = {'session_id': 'test', 'type_name': 'test_type'}
    rv = self.app.post('/api/assets/types', data=data, follow_redirects=True)
    if (sys.version_info > (3,)):
      type = jsonpickle.decode(rv.data.decode('utf-8'))
    else: 
      type = jsonpickle.decode(rv.data)
    self.assertIsNotNone(type, 'No type returned')
    self.logger.info('[%s] Type: %s\n', method, type)

  def test_types_get_by_id(self):
    method = 'test_types_get_by_id'
    rv = self.app.get('/api/assets/types/1?session_id=test')
    if (sys.version_info > (3,)):
      asset_type = jsonpickle.decode(rv.data.decode('utf-8'))
    else: 
      asset_type = jsonpickle.decode(rv.data)
    self.assertIsNotNone(asset_type, 'No asset type returned')
    self.logger.info('[%s] Asset Type: %s\n', method, asset_type)

  def test_types_patch(self):
    method = 'test_types_patch'
    data = {'session_id': 'test', 'type_name': 'test_type_patch'}
    rv = self.app.patch('/api/assets/types/1', data=data, follow_redirects=True)
    if (sys.version_info > (3,)):
      asset_type = jsonpickle.decode(rv.data.decode('utf-8'))
    else: 
      asset_type = jsonpickle.decode(rv.data)
    self.assertIsNotNone(asset_type, 'No asset type returned')
    self.logger.info('[%s] Asset Type: %s\n', method, asset_type)

  def test_types_delete(self):
    method = 'test_types_delete'
    rv = self.app.delete('/api/assets/types/1?session_id=test')
    self.assertIsNone(jsonpickle.decode(rv.data), 'Asset type not deleted')
    self.logger.info('[%s] Asset Type: deleted\n', method)  # THIS LINE IS MISSING

  def test_types_get_by_name(self):
    method = 'test_types_get_by_name'
    rv = self.app.get('/api/assets/types/test_type?session_id=test')
    if (sys.version_info > (3