
def search(lst):
    if not lst:
        return -1
    max_freq = 0
    for i, num in enumerate(lst):
        if num > max_freq:
            max_freq = num
    if max_freq < 1:
        return -1
    for num in lst:
        if num == max_freq:
            return num
    return -1