def count_Occurrence(tup, lis):
    count_dict = {}
    for item in lis:
        count_dict[item] = tup.count(item)
    return sum(count_dict.values())  # Return the sum of all counts