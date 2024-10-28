def filter_data(students, min_height, min_weight):
    filtered_students = {name: info for name, info in students.items() if info[0] >= min_height and info[1] >= min_weight}
    return filtered_students