def drop_empty(input_dict):
    return {key: value for key, value in input_dict.items() if value is not None}  # Filter out None values