from collections import Counter
def max_occurrences(lst):
    return Counter(lst).most_common(1)[0][0] if lst else None