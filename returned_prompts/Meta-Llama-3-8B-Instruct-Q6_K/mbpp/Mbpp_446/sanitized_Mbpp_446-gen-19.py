def count_Occurrence(tup, lst):
    count_dict = {}
    for i in tup:
        if i in lst:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
    return sum(count_dict.values())