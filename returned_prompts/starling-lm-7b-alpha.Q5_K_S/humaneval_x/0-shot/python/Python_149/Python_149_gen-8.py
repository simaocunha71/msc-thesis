
def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0]
    lst.sort(key=len)
    return lst

# Testing
print(sorted_list_sum(["aa", "a", "aaa"]))  # Output: ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # Output: ["ab", "cd"]








def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0]
    lst.sort(key=lambda word: (len(word), word))
    return lst

# Testing
print(sorted_list_sum(["aa", "a", "aaa"]))  # Output: ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # Output: ["ab", "cd"]







def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0]
    lst.sort(key=lambda word: (len(word), word))
    return lst

# Testing
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]







def sorted_list_sum(lst):
    lst = [word for word in lst if len(word) % 2 == 0]
    lst.sort(key=lambda word: (len(word), word))
    return lst

# Testing
print(sorted_list_sum(["aa", "a", "aaa"]))  # Output: ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # Output: ["ab", "cd"]






def sorted_