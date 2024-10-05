
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    lst = [word for word in lst if len(word) % 2 == 0]
    lst = sorted(lst, key=len)
    return lst

# Testing:
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
assert sorted_list_sum(["ac", "cd", "ab", "dc"]) == ["ab", "ac", "cd", "dc"]
assert sorted_list_sum(["abc", "abcde", "abcd"]) == ["abc", "abcd", "abcde"]

# Extra:
# assert sorted_list_sum(["a", "aa", "aaa"]) == ["a", "aa", "aaa"]
# assert sorted_list_sum(["ab", "cd"]) == ["ab", "cd"]
# assert sorted_list_sum(["cd", "ab"]) == ["ab", "cd"]


# Here is the Pythonic way of doing this:
# def sorted_list_sum(lst):
#     """Write a function that accepts a list of strings as a parameter,
#     deletes the strings that have odd lengths from it,
#     and returns the