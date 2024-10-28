def filter_data(data: dict, min_height: float, min_weight: float) -> dict:
  new_data = {}
  for key, value in data.items():
    if value[0] > min_height and value[1] > min_weight:
      new_data[key] = value
  return new_data