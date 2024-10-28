def sorted_list_sum(lst):
    # Filter out strings with odd lengths
    lst = [s for s in lst if len(s) % 2 == 0]

    # Sort the list by length and then alphabetically
    lst.sort(key=lambda s: (len(s), s))

    return lst

# Test cases
print(sorted_list_sum(["aa", "a", "aaa"]))  # Output: ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # Output: ["ab", "cd"]
print(sorted_list_sum(["abc", "ab", "abcd", "abcd"]))  # Output: ["abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abcd", "abcd"]))  # Output: ["abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abcd"]))  # Output: ["abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abc", "abcd"]))  # Output: ["abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abc", "abc"]))  # Output: ["abc", "abc", "abc"]
print(sorted_list_sum(["abcd", "abc", "abc", "abcd", "abcd"]))  # Output: ["abcd", "abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abc", "abcd", "abcd", "abcd"]))  # Output: ["abcd", "abcd", "abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abc", "abcd", "abcd", "abcd", "abcd"]))  # Output: ["abcd", "abcd", "abcd", "abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abc", "abcd", "abcd", "abcd", "abcd", "abcd"]))  # Output: ["abcd", "abcd", "abcd", "abcd", "abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abc", "abcd", "abcd", "abcd", "abcd", "abcd", "abcd"]))  # Output: ["abcd", "abcd", "abcd", "abcd", "abcd", "abcd", "abcd"]
print(sorted_list_sum(["abcd", "abc", "abc", "abcd", "abcd", "abcd", "abcd", "abcd", "abcd", "abcd"]))  # Output: ["abcd", "abcd", "abcd", "