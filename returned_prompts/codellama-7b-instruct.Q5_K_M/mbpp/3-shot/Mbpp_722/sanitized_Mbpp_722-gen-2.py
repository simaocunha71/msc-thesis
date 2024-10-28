def filter_data(data: dict, height: float, weight: float) -> dict:
  filtered_data = {key: val for key, val in data.items() if val[0] >= height and val[1] >= weight}
  return filtered_data