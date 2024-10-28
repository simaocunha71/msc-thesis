def extract_singly(list_of_tuples):
    result = []
    for tup in list_of_tuples:
        result.extend(tup)
    return set(result)