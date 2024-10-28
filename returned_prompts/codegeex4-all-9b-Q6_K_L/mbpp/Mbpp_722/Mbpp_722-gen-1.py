def filter_data(data: dict, min_height: float, min_weight: float) -> dict:
  filtered_data = {name: info for name, info in data.items() if info[0] >= min_height and info[1] >= min_weight}
  return filtered_data

