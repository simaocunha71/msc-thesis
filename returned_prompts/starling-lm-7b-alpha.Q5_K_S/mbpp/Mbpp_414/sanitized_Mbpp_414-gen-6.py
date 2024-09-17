from collections import Counter
def overlapping(list_1, list_2):
    c = Counter(list_1)
    return any(i in c for i in list_2)