def sorted_list_sum(lst):
    return sorted([x for x in lst if len(x) % 2 == 0], key=lambda x: (len(x), x))

print(sorted_list_sum(["aa", "a", "aaa"]))
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))
print(sorted_list_sum(["ab", "a", "aaa", "cd", "abcd", "abcde", "abc"]))
print(sorted_list_sum(["ab", "a", "aaa", "cd", "abcd", "abcde", "abc", "abcda", "abcde", "abcde", "abcde", "abcde"]))