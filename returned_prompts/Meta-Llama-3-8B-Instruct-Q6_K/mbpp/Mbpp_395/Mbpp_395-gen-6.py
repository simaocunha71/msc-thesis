```
def first_non_repeating_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None
```   



This function works by first counting the occurrences of each character in the string. Then, it iterates over the string again to find the first character that has a count of 1. If no such character is found, the function returns None. The unit test `assert first_non_repeating_character("abcabc") == None` ensures that the function correctly handles strings where no character appears only once.  



The time complexity of this function is O(n), where n is the length of the input string, because it iterates over the string twice. The space complexity is also O(n), because it stores the count of each character in a dictionary.  



The provided unit test can be run using Python's built-in `assert` statement, which will raise an AssertionError if the function does not return the expected result. This can be useful for testing the function and ensuring that it behaves as expected.  



Here is an example of how to use the function:
```
print(first_non_repeating_character("abcde"))  # Output: 'a'
print(first_non_repeating_character("abcabc"))  # Output: None
```   



This example demonstrates the function's ability to find the first non-repeating character in a string and return None if no such character exists.  



The function can be modified to return all non-repeating characters instead of just the first one. This could be done by storing the non-repeating characters in a list and returning the list. Here is an example of how this could be done:
```
def all_non_repeating_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    non_repeating_chars = [char for char in s if char_count[char] == 1]
    
    return non_repeating_chars
```
This function returns a list of all non-repeating characters in the input string. If the string contains no non-repeating characters, the function returns an empty list.  



The time complexity of this function is still O(n),