
def merge_dictionaries_three(d1: dict, d2: dict, d3: dict) -> dict:
    merged_dict = {}
    merged_dict.update(d1)
    merged_dict.update(d2)
    merged_dict.update(d3)
    return merged_dict


