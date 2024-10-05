
def search(lst):
    freq = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
    for x in lst:
        if x > 0 and freq[x] >= x:
            return x
    return -1
