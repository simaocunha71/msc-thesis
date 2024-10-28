from collections import Counter
def frequency_lists(arr):
    return Counter(item for sublist in arr for item in sublist)