from collections import Counter
def max_occurrences(lst):
    return max(Counter(lst).values())  # returns the maximum frequency