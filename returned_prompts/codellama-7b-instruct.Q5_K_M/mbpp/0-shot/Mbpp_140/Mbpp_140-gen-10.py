def extract_singly(list_of_lists):
    return {item for sublist in list_of_lists for item in sublist}
