def filter_data(data: dict, min_height: float, min_weight: int) -> dict:
  return {k: v for k, v in data.items() if v[0] > min_height and v[1] > min_weight}