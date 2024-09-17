
def filter_data(students: dict, min_height: float, min_weight: float) -> dict:
  return {name: info for name, info in students.items() if info[0] >= min_height and info[1] >= min_weight}


