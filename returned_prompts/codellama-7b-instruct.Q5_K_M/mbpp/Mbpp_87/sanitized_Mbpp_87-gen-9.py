def merge_dictionaries_three(*dicts):
    final_dict = {}
    for d in dicts:
        final_dict.update(d)
    return final_dict