def max_occurrences(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_count = max(count.values())
    for key in count:
        if count[key] == max_count:
            return key