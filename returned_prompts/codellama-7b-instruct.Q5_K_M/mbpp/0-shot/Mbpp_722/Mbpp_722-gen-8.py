def filter_data(student_data, min_height, min_weight):
    return {name: height_weight for name, height_weight in student_data.items() if height_weight[0] >= min_height and height_weight[1] >= min_weight}
