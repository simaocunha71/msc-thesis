def check_occurences(tuples_list):
    from collections import Counter
    counter = Counter(tuples_list)
    result = {}
    for key, value in counter.items():
        result[key] = value
    return result