
def search(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i in freq:
        if freq[i] >= i and i > 0:
            return i

    return -1
