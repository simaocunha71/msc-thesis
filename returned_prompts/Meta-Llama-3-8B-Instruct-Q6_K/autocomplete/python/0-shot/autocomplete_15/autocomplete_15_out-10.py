  # [POST] Response data: %s

    if rv.status_code == 201:  # created
      self.logger.info('Asset Type created successfully')
      response_json = jsonpickle.decode(postResponse, unpicklable=False)
      self.logger.debug('Response JSON: %s', response_json)
      self.asset_type_id = response_json['id']
      self.logger.info('Asset Type ID: %s', self.asset_type_id)

    elif rv.status_code == 400:  # bad request
      self.logger.info('Error creating Asset Type: %s', postResponse)
      self.asset_type_id = None
    else:
      self.logger.error('Unexpected status code: %s', rv.status_code)
      self.asset_type_id = None
    return self.asset_type_id

    # This is where I'm stuck. I need to add code to handle the response
    # based on the status code. If 201, set self.asset_type_id to the
    # response JSON's 'id' value. If 400, set self.asset_type_id to None.
    # If any other status code, set self.asset_type_id to None and log
    # an error message.

    if rv.status_code == 201:
      self.asset_type_id = response_json['id']
    elif rv.status_code == 400:
      self.asset_type_id = None
    else:
      self.logger.error('Unexpected status code: %s', rv.status_code)
      self.asset_type_id = None


    self.logger.info('Asset Type ID: %s', self.asset_type_id)
    return self.asset_type_id

    # This is where I'm stuck. I need to add code to handle the response
    # based on the status code. If 201, set self.asset_type_id to the
    # response JSON's 'id' value. If 400, set self.asset_type_id to None.
    # If any other status code, set self.asset_type_id to None and log
    # an error message.

    if rv.status_code == 201:
        self.asset_type_id = response_json['id']
    elif rv.status_code == 400:
        self.asset_type_id = None
    else:
        self.logger.error('Unexpected status code: %s', rv.status_code)
        self.asset_type_id = None

    self.logger.info('Asset Type ID: %s', self.asset_type_id)
    return self.asset_type_id

    #