def filter_data(student_data: dict, min_height: float, min_weight: float) -> dict:
    return {name: data for name, data in student_data.items() if data[0] >= min_height and data[1] >= min_weight}