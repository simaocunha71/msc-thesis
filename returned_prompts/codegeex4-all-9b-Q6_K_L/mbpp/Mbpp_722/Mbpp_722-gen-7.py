def filter_data(students: dict,height: float,weight: float) -> dict:
  return {name: data for name, data in students.items() if data[0] > height and data[1] > weight}

