def max_occurrences(lst):
    count_dict = {i: lst.count(i) for i in lst}
    max_value = max(count_dict.values())
    return [k for k, v in count_dict.items() if v == max_value]