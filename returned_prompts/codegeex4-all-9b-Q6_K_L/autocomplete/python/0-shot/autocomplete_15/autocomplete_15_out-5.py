```python
    if rv.status_code != 200:
      self.logger.error('[%s] Failed to add new asset type.', method)
      raise Exception('Failed to add new asset type.')
    self.logger.info('[%s] Successfully added new asset type.', method)
    return json.loads(postResponse)
```