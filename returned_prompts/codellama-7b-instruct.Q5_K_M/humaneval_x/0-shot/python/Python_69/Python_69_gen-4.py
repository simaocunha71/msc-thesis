
def search(lst):
    lst_freq = {}
    for i in lst:
        if i in lst_freq:
            lst_freq[i] += 1
        else:
            lst_freq[i] = 1

    for i in lst_freq:
        if lst_freq[i] >= i and lst_freq[i] > 0:
            return i

    return -1