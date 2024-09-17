def filter_data(student_data: dict,min_height: float,min_weight: float) -> dict:
  filtered_data = {name: (height, weight) for name, (height, weight) in student_data.items() if height >= min_height and weight >= min_weight}
  return filtered_data

