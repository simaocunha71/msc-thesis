def max_occurrences(lst):
    # count the occurrences of each item in the list
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    # find the item with the maximum count
    max_count = 0
    max_item = None
    for item, count in counts.items():
        if count > max_count:
            max_count = count
            max_item = item

    return max_item