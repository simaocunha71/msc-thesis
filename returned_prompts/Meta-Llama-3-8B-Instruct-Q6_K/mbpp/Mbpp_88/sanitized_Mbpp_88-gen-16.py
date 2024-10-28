def freq_count(lst):
    freq = {}
    for element in set(lst):
        freq[element] = lst.count(element)
    return freq