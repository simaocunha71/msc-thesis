def find_sum(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return sum([num for num in count_dict if count_dict[num] == 1])