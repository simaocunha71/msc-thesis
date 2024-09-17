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
```  # Return None if no non-repeating character is found
```
This function works by first counting the occurrences of each character in the string. Then it iterates over the string again, and returns the first character that has a count of 1. If no such character is found, it returns None. The unit test `assert first_non_repeating_character("abcabc") == None` ensures that the function returns None if no non-repeating character is found. 