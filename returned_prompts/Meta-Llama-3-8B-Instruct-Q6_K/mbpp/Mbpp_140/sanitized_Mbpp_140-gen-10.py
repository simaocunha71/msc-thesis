def extract_singly(lst):
    flat_list = [item for sublist in lst for item in sublist]
    return set(flat_list)  # or return set(flat_list) if you want to remove duplicates