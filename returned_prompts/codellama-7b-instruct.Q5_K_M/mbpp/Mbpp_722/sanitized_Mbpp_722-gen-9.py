def filter_data(data, min_height, min_weight):
    return {student: (height, weight) for student, (height, weight) in data.items() if height >= min_height and weight >= min_weight}