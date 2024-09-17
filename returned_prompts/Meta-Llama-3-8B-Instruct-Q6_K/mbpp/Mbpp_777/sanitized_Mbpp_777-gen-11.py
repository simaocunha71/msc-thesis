def find_sum(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    sum = 0
    for i in count_dict:
        if count_dict[i] == 1:
            sum += i
    return sum