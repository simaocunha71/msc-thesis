def filter_data(dict_of_students, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in dict_of_students.items() if height >= min_height and weight >= min_weight}