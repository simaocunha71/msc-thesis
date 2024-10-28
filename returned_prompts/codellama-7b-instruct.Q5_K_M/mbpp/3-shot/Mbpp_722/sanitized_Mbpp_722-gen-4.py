def filter_data(student_data, minimal_height, minimal_weight):
  filtered_data = {name: (height, weight) for name, (height, weight) in student_data.items() if height >= minimal_height and weight >= minimal_weight}
  return filtered_data