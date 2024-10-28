def max_occurrences(lst):
    from collections import Counter
    counter = Counter(lst)
    max_freq = max(counter.values())
    max_items = [item for item, freq in counter.items() if freq == max_freq]
    return max_items[0]