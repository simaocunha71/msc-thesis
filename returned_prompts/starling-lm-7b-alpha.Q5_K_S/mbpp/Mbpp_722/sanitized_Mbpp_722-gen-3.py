def filter_data(data,min_height,min_weight):
    """
    Args:
        data: dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value
        min_height: minimal height
        min_weight: minimal weight
    Returns:
        dictionary with the names of the students who have a height and a weight above the minimum
    """
    result = {}
    for key,value in data.items():
        if value[0]>min_height and value[1]>min_weight:
            result[key] = value
    return result