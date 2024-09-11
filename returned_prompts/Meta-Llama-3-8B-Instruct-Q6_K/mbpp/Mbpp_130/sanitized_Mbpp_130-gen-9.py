from collections import Counter
def max_occurrences(lst):
    freq = Counter(lst)
    return max(freq, key=freq.get)  # Returns the most common element and its count