def extract_singly(lst):
    return set([item for sublist in lst for item in sublist])  # flatten the list of lists into a single set of numbers