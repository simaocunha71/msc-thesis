      assets = jsonpickle.loads(rv.data.decode('utf-8'))
    json_resp = json.loads(rv.data.decode('utf-8'))
    if rv.status_code != 200:
      self.logger.warn('[%s] Expected 200 OK, got %s', method, rv.status_code)
      raise AssertionError()
    if 'message' in json_resp:
      message = json_resp.get('message', None)
      self.assertIsNotNone(message, 'No message returned')
      self.logger.info('[%s] Message: %s\n', method, message)
    if 'data' not in json_resp:
      self.logger.warn('[%s] Expected data, got none', method)
      raise AssertionError()
    if (sys.version_info > (3,)):
      assets = jsonpickle.decode(json_resp['data'])
    else:
      assets = jsonpickle.loads(json_resp['data'])
    for a in assets:
      self.logger.info('[%s] asset: %s', method, a)
      self.assertIsInstance(a, dict)
      self.assertEqual(a['id'], a['id'])
      self.assertEqual(a['name'], a['name'])
      if 'description' in a:
        self.assertEqual(a['description'], a['description'])
      if 'category' in a:
        self.assertEqual(a['category'], a['category'])
        if 'subcategory' in a:
          self.assertEqual(a['subcategory'], a['subcategory'])
      if 'type' in a:
        self.assertEqual(a['type'], a['type'])
        if 'subtype' in a:
          self.assertEqual(a['subtype'], a['subtype'])
      if 'unit' in a:
        self.assertEqual(a['unit'], a['unit'])
      if 'min' in a:
        self.assertEqual(a['min'], a['min'])
      if 'max' in a:
        self.assertEqual(a['max'], a['max'])
      if 'step' in a