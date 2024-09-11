def drop_empty(dictionary):
    return {k: v for k, v in dictionary.items() if v is not None}  # Remove items with None values