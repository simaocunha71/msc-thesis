"""
def first_non_repeating_character(str):
    '''
    This function will return the first non-repeated character in the string
    '''
    # Create a dictionary to count the occurrence of each character
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Traverse the string and find the first non-repeated character
    for char in str:
        if char_count[char] == 1:
            return char

    # Return None if no non-repeated character is found
    return None

"""
This function works by first creating a dictionary to count the occurrence of each character in the string. Then, it traverses the string again and returns the first character that has a count of 1 in the dictionary, indicating that it is the first non-repeated character. If no such character is found, it returns None.

Here are some usage examples:

print(first_non_repeating_character("abcabc"))  # None
print(first_non_repeating_character("abcd"))    # a
print(first_non_repeating_character("abacd"))   # b

"""

# Important Note: This solution has a time complexity of O(n), where n is the length of the input string. This is because it needs to traverse the string twice. However, it has a space complexity of O(1) since it only uses a fixed amount of extra space to store the count of each character.

# Here are some additional test cases to validate the function:

def test_first_non_repeating_character():
    assert first_non_repeating_character("abcabc") == None
    assert first_non_repeating_character("abcd") == "a"
    assert first_non_repeating_character("abacd") == "b"
    assert first_non_repeating_character("") == None
    assert first_non_repeating_character("aa") == None
    print("All test cases pass")

test_first_non_repeating