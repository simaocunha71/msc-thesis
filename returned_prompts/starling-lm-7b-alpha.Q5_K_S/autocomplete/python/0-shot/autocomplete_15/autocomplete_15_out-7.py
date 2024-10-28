    if (postResponse.startswith('2')):
      self.session_id = rv.json['session_id']
      self.asset_type_id = rv.json['object']['id']
      return True
    else:
      self.logger.error('[%s] Response code: %s', method, postResponse)
      self.logger.error('[%s] Response error: %s', method, rv.json['error']['message'])
      return False

