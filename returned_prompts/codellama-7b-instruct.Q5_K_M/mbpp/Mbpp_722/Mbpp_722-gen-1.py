
def filter_data(student_data: dict, height: float, weight: float) -> dict:
  filtered_data = {}
  for name, values in student_data.items():
    if values[0] >= height and values[1] >= weight:
      filtered_data[name] = values
  return filtered_data


