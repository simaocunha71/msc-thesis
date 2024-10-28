def filter_data(students, min_height, min_weight):
    filtered_students = {name: height_weight for name, height_weight in students.items() if height_weight[0] > min_height and height_weight[1] > min_weight}
    return filtered_students