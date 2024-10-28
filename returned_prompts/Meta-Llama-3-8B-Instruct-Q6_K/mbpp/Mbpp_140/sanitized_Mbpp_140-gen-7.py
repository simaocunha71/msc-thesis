def extract_singly(lst):
    flat_list = [item for sublist in lst for item in sublist]
    return set(flat_list)  # convert the list to a set for uniqueness