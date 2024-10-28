def frequency_lists(lists):
    freqs = {}
    for sublist in lists:
        for item in sublist:
            if item in freqs:
                freqs[item] += 1
            else:
                freqs[item] = 1
    return freqs