def extract_singly(list_of_lists):
    return set([i for sublist in list_of_lists for i in sublist])  # Python 3.9+
    # return set([i for sublist in list_of_lists for i in sublist]).union(*[set(sublist) for sublist in list_of_lists])  # For Python 3.8 and below