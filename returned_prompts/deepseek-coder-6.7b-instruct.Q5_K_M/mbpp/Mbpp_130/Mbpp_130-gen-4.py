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

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])) # should return 2

"""


"""

