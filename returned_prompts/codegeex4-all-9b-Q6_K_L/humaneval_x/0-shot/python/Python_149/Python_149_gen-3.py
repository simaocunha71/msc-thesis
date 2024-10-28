def sorted_list_sum(lst):
    return sorted([x for x in lst if len(x) % 2 == 0])

print(sorted_list_sum(["aa", "a", "aaa"])) # => ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"])) # => ["ab", "cd"]
print(sorted_list_sum(["ab", "a", "aaa", "cd", "a", "ab"])) # => ["ab", "ab", "cd"]
print(sorted_list_sum(["ab", "a", "aaa", "cd", "a", "ab", "abcd"])) # => ["ab", "ab", "cd", "abcd"]