def filter_data(data: dict, height: float, weight: float) -> dict:
  return {k: v for k, v in data.items() if v[0] > height and v[1] > weight}