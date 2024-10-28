def merge_dictionaries_three(d1,d2,d3):
    merged_dict = d1.copy()
    merged_dict.update(d2)
    merged_dict.update(d3)
    return merged_dict