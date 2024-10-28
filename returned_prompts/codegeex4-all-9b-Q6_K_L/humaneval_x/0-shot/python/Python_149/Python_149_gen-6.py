def sorted_list_sum(lst):
    new_list = [item for item in lst if len(item) % 2 == 0]
    new_list.sort(key=lambda x: (len(x), x))
    return new_list

print(sorted_list_sum(["aa", "a", "aaa"]))
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))