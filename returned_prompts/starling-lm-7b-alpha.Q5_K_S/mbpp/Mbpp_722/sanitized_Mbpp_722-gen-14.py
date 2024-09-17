def filter_data(student_info, min_height, min_weight):
  return {k: v for k, v in student_info.items() if v[0] > min_height and v[1] > min_weight}