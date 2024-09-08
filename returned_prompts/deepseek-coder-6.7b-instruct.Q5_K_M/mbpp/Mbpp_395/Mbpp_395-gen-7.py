def first_non_unique_character(s):
    count_dict = {}
    for i in s:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    for i in s:
        if count_dict[i] > 1:
            return