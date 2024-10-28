    if (rv.status_code != 200):
      self.logger.error('API call %s failed with status code %d', url, rv.status_code)
      raise Exception('[%s] API call failed with status code %d' % (method, rv.status_code))
    else:
      self.logger.info('API call %s succeeded with status code %d', url, rv.status_code)

