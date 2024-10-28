def extract_singly(lst):
    return set([i for sublist in lst for i in sublist])  # flatten and convert to set