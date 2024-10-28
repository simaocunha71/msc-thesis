def sorted_list_sum(lst):
    return sorted([x for x in lst if len(x) % 2 == 0])

print(sorted_list_sum(["aa", "a", "aaa"]))
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))