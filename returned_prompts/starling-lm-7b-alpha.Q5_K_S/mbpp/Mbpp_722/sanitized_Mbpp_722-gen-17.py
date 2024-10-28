def filter_data(data: dict, h_min: float, w_min: float) -> dict:
  result = {}
  for key, value in data.items():
    if value[0] > h_min and value[1] > w_min:
      result[key] = value
  return result