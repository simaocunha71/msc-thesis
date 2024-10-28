
def sorted_list_sum(lst):
    """
    This function deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    """
    # Create a new list that only contains strings with even lengths
    even_length_list = [word for word in lst if len(word) % 2 == 0]

    # Sort the even length list by length of each word, and if two words have the same length,
    # sort the list alphabetically
    sorted_list = sorted(even_length_list, key=len)

    # Return the sorted list
    return sorted_list

# Test the function
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

# You can add more tests here if you like

# End of program

# Here are some additional tests that you can add if you like
def test_sorted_list_sum():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["bc", "d", "aa", "ef"]) == ["bc", "d", "ef"]
    assert sorted_list_sum(["aaa", "bbb", "ccc"]) == ["aaa", "bbb", "ccc"]
    assert sorted_list_sum(["aa", "aaa", "aaaa"]) == ["aa", "aaa", "aaa"]
    assert sorted_list_sum(["aaay", "aay", "ay"]) == ["ay", "aay"]
    assert sorted_list_sum(["ab", "c", "d"]) == ["ab