
def filter_data(students, min_height, min_weight):
  result = {}
  for name, (height, weight) in students.items():
    if height > min_height and weight > min_weight:
      result[name] = (height, weight)
  return result


