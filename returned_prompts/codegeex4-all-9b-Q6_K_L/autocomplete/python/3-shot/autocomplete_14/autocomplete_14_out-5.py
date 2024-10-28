  
      assets = jsonpickle.decode(rv.data)
    self.logger.info('[%s] Assets: %s\n', method, assets)
    self.assertEqual(rv.status_code, 200)

  def test_types_post(self):
    method = 'test_types_post'
    rv = self.app.post('/api/assets/types?session_id=test', content_type='application/json', data=json.dumps({
      "type": "test type",
      "description": "test type description"
    }))
    if (sys.version_info > (3,)):
      json_resp = jsonpickle.decode(rv.data.decode('utf-8'))
    else:  
      json_resp = jsonpickle.decode(rv.data)
    message = json_resp.get('message', None)
    self.assertIsNotNone(message, 'No message returned')
    self.logger.info('[%s] Message: %s\n', method, message)
    self.assertEqual(rv.status_code, 200)

  def test_types_get_with_id(self):
    method = 'test_types_get_with_id'
    rv = self.app.get('/api/assets/types/1?session_id=test')
    if (sys.version_info > (3,)):
      assets = jsonpickle.decode(rv.data.decode('utf-8'))
    else:  
      assets = jsonpickle.decode(rv.data)
    self.logger.info('[%s] Assets: %s\n', method, assets)
    self.assertEqual(rv.status_code, 200)

  def test_types_put(self):
    method = 'test_types_put'
    rv = self.app.put('/api/assets/types/1?session_id=test', content_type='application/json', data=json.dumps({
      "type": "test type",
      "description": "test type description"
    }))
    if (sys.version_info > (3,)):
      json_resp = jsonpickle.decode(rv.data.decode('utf-8'))
    else:  
      json_resp = jsonpickle.decode(rv.data)
    message = json_resp.get('message', None)
    self.assertIsNotNone(message, 'No message returned')
    self.logger.info('[%s] Message: %s\n', method, message)
    self.assertEqual(rv.status_code, 200)

  def test_types_delete(self):
    method = 'test_types_delete'
    rv = self.app.delete('/api/assets/types/1?session_id=test')
    if (sys.version_info > (3,)):
      json_resp = jsonpickle.decode(rv.data.decode('utf-8'))
    else:  
      json_resp = jsonpickle.decode(rv.data)
