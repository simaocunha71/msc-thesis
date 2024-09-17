def filter_data(data: dict, height: float, weight: float) -> dict:
  return {name: val for name, val in data.items() if all(i >= height for i in val) and all(i >= weight for i in val)}