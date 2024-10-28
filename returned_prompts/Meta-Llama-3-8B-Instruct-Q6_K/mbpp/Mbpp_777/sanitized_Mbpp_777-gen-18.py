def find_sum(lst):
    count_dict = {}
    for x in lst:
        count_dict[x] = count_dict.get(x, 0) + 1
    return sum(x for x in count_dict if count_dict[x] == 1)