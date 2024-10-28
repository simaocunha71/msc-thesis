
def filter_data(students_data, min_height, min_weight):
  return {name: data for name, data in students_data.items() if data[0] >= min_height and data[1] >= min_weight}


