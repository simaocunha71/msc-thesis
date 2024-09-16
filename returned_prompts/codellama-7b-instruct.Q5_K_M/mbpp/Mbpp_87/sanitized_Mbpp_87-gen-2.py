def merge_dictionaries_three(*dictionaries):
    merged_dict = {}
    for dictionary in dictionaries:
        merged_dict.update(dictionary)
    return merged_dict