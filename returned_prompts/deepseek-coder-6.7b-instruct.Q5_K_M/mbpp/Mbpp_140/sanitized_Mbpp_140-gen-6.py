def extract_singly(lst):
    flattened = []
    for sublist in lst:
        for item in sublist:
            flattened.append(item)
    return flattened