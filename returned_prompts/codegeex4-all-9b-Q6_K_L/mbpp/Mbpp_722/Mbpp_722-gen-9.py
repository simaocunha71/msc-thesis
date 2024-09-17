def filter_data(students: dict, height: float, weight: float) -> dict:
  filtered_students = {name: height_weight for name, height_weight in students.items() if height_weight[0] >= height and height_weight[1] >= weight}
  return filtered_students

