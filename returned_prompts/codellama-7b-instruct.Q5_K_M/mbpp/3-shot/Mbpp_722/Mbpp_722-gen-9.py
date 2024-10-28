
def filter_data(student_data: dict, min_height: float, min_weight: float) -> dict:
  return {k: v for k,v in student_data.items() if v[0] >= min_height and v[1] >= min_weight}


