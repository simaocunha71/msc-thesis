
def filter_data(student_data: dict,height: float,weight: int) -> dict:
  filtered_data = {name: (height, weight) for name, (height, weight) in student_data.items() if height > height and weight > weight}
  return filtered_data


