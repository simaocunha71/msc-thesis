def max_occurrences(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    max_frequency = max(count_dict.values())
    for key, value in count_dict.items():
        if value == max_frequency:
            return key