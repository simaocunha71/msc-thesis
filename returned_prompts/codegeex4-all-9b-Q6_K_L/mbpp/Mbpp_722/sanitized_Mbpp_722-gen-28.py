def filter_data(student_dict: dict, min_height: float, min_weight: float) -> dict:
  return {name: info for name, info in student_dict.items() if info[0] >= min_height and info[1] >= min_weight}