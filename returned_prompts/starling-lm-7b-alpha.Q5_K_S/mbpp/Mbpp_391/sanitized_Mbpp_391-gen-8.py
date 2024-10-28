def convert_list_dictionary(list_1, list_2, list_3):
    """Converts a given list of lists to a nested dictionary."""
    # Assuming each list has equal length
    assert len(list_1) == len(list_2) == len(list_3)

    result = {}
    for index, item in enumerate(list_1):
        result[item] = {}
        result[item][list_2[index]] = list_3[index]

    return result