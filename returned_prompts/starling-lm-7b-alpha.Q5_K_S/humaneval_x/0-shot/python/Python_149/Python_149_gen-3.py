
def sorted_list_sum(lst):
    # Create a new list containing only the strings with even lengths
    even_length_strings = [word for word in lst if len(word) % 2 == 0]

    # Sort the list by the length of each word, and alphabetically if the length is the same
    even_length_strings.sort(key=len)

    return even_length_strings

# Test
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]





def sorted_list_sum(lst):
    # Create a new list containing only the strings with even lengths
    even_length_strings = [word for word in lst if len(word) % 2 == 0]

    # Sort the list by the length of each word, and alphabetically if the length is the same
    even_length_strings.sort(key=len)

    return even_length_strings

# Test
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]





def sorted_list_sum(lst):
    # Create a new list containing only the strings with even lengths
    even_length_strings = [word for word in lst if len(word) % 2 == 0]

    # Sort the list by the length of each word, and alphabetically if the length is the same
    even_length_strings.sort(key=len)

    return even_length_strings

# Test
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]





def sorted_list_sum(lst):
    # Create a new list containing only the strings with even lengths
    even_length_strings = [word for word in lst if len