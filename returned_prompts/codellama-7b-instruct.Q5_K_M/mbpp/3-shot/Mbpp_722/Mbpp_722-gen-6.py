
def filter_data(students_data: dict,min_height: float,min_weight: float) -> dict:
  filtered_students = {student: data for student, data in students_data.items() if data[0] >= min_height and data[1] >= min_weight}
  return filtered_students


