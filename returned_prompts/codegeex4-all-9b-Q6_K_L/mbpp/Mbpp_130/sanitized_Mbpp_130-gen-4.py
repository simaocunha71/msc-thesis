def max_occurrences(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    max_key = max(count, key=count.get)
    return max_key