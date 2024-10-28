def check_occurences(lst):
    freq = {}
    for tup in lst:
        if tup in freq:
            freq[tup] += 1
        else:
            freq[tup] = 1
    return freq

