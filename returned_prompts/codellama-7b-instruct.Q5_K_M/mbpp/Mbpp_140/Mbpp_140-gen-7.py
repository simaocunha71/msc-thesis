def extract_singly(list_of_lists):
    return {x for sublist in list_of_lists for x in sublist}
