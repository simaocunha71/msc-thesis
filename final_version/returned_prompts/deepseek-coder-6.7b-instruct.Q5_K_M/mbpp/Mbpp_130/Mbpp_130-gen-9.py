def max_occurrences(lst):
    count_dict = {i: lst.count(i) for i in lst}
    max_value = max(count_dict.values())
    return [k for k, v in count_dict.items() if v == max_value]

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))


