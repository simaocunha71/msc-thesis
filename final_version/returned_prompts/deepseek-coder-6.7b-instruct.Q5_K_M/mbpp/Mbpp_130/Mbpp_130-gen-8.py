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

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])) # 2

"""
