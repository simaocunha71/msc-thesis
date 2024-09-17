def extract_singly(my_list):
    result = set()
    for sublist in my_list:
        result.update(sublist)
    return result