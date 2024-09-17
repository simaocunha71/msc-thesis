def max_occurrences(lst):
    counts = {}
    for i in lst:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    max_count = max(counts.values())
    for k,v in counts.items():
        if v == max_count:
            return k