def filter_data(data: dict, min_height: float, min_weight: float) -> dict:
  return {key: value for key, value in data.items() if value[0] >= min_height and value[1] >= min_weight}