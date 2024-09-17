def filter_data(students_data, min_height, min_weight):
    return {name: info for name, info in students_data.items() if info[0] >= min_height and info[1] >= min_weight}