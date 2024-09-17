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


The function `first_non_repeating_character` takes a string `s` as input and returns the first non-repeating character in the string. If no non-repeating character is found, it returns `None`.

The function works by first counting the occurrences of each character in the string using a dictionary `char_count`. Then, it iterates over the string again and returns the first character that has a count of 1 in the `char_count` dictionary. If no such character is found, it returns `None`.

The unit test `assert first_non_repeating_character("abcabc") == None` ensures that the function returns `None` when no non-repeating character is found. This test case is important because it demonstrates the edge case where the input string contains all repeated characters. In this case, the function should return `None` because there is no non-repeating character.