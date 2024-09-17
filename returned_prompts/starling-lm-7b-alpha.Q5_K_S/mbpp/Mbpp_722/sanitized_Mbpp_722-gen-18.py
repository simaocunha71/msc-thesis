def filter_data(student_data: dict,min_height: float, min_weight: int) -> dict:
  filtered_data = {}
  for name, (height, weight) in student_data.items():
    if height > min_height and weight > min_weight:
      filtered_data[name] = (height, weight)
  return filtered_data