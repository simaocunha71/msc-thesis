def filter_data(student_data, min_height, min_weight):
    return {student: data for student, data in student_data.items() if data[0] >= min_height and data[1] >= min_weight}