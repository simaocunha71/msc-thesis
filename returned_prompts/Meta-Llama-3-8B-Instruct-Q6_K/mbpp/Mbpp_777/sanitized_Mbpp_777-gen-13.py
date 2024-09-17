def find_sum(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    sum_non_repeated = 0
    for key, value in count_dict.items():
        if value == 1:
            sum_non_repeated += key
    return sum_non_repeated