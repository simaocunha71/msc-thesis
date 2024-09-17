
def filter_data(students: dict, min_height: float, min_weight: float) -> dict:
  return {name: data for name, data in students.items() if data[0] >= min_height and data[1] >= min_weight}


