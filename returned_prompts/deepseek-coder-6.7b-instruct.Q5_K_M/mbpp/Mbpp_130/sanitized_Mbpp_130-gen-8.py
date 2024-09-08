def max_occurrences(lst):
    max_count = 0
    max_item = None
    count_dict = {}

    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

        if count_dict[item] > max_count:
            max_count = count_dict[item]
            max_item = item

    return max_item