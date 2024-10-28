def find_sum(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    sum = 0
    for key, value in count_dict.items():
        if value == 1:
            sum += key
    return sum