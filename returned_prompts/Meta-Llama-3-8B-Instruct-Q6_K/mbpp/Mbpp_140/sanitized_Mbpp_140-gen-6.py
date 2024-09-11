def extract_singly(list_of_lists):
    flat_list = [item for sublist in list_of_lists for item in sublist]
    return set(flat_list)  # convert to set to remove duplicates