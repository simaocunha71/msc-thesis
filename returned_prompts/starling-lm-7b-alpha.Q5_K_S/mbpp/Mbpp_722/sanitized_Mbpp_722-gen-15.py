def filter_data(student_dict,min_height,min_weight):
  return {key:value for (key,value) in student_dict.items() if value[0] > min_height and value[1] > min_weight}