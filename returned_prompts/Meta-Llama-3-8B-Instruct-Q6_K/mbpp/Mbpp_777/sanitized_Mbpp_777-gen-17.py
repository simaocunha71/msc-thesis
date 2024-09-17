def find_sum(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    sum = 0
    for num, count in count_dict.items():
        if count == 1:
            sum += num

    return sum