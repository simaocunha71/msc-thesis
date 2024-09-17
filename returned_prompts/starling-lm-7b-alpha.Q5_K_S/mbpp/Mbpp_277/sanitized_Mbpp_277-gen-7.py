def dict_filter(dictionary, n):
    new_dict = {}
    for key, value in dictionary.items():
        if value >= n:
            new_dict[key] = value
    return new_dict