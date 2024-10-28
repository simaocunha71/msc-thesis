
def filter_data(data: dict, height: float, weight: float) -> dict:
  result = {name: (height, weight) for name, (height, weight) in data.items() if height > 6.0 and weight > 70}
  return result


