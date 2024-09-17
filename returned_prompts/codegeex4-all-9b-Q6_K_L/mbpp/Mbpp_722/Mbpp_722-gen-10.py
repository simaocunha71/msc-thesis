def filter_data(students, min_height, min_weight):
    filtered_students = {name: data for name, data in students.items() if data[0] >= min_height and data[1] >= min_weight}
    return filtered_students

