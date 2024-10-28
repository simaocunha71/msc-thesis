      assets = jsonpickle.decode(rv.data)

    self.assertIsNotNone(assets, 'No assets returned')
    self.logger.info('[%s] Assets: %s\n', method, assets)

