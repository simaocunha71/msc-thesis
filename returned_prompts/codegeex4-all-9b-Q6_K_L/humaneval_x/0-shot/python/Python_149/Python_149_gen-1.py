def sorted_list_sum(lst):
    return sorted([word for word in lst if len(word) % 2 == 0])

print(sorted_list_sum(["aa", "a", "aaa"]))  # => ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # => ["ab", "cd"]