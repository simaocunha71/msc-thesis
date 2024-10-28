from collections import Counter
def max_occurrences(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max_freq = max(count.values())
    for key, value in count.items():
        if value == max_freq:
            return key