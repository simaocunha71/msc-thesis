    if rv.status_code == 201:
        new_asset_type_json = jsonpickle.decode(rv.data)
        new_asset_type_id = new_asset_type_json['asset_type_id']
        self.logger.info('[%s] Created asset type with id: %s', method, new_asset_type_id)
        return new_asset_type_id
    elif rv.status_code == 409:
        self.logger.warning('[%s] Asset type with name \'%s\' already exists', method, new_asset_type_name)
    else:
        self.logger.error('[%s] Failed to create asset type', method)

