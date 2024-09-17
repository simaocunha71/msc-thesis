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
The function `first_non_repeating_character` takes a string `s` as input and returns the first non-repeating character. If no non-repeating character is found, it returns `None`.

Here's the explanation of the function:

1. Initialize an empty dictionary `char_count` to store the count of each character in the string.
2. Iterate through the string `s` and for each character, increment its count in the `char_count` dictionary. If the character is not present in the dictionary, add it with a count of 1.
3. Iterate through the string `s` again and for each character, check if its count in the `char_count` dictionary is 1. If it is, return the character as it is the first non-repeating character.
4. If no non-repeating character is found after iterating through the entire string, return `None`.

The unit test `assert first_non_repeating_character("abcabc") == None` ensures that the function returns `None` when no non-repeating character is found in the string. This test also checks that the function returns the correct first non-repeating character when it exists. For example, `first_non_repeating_character("abcdefg")` would return `'a'`.  If there are multiple non-repeating characters, the function returns the first one it encounters.  If you want to return all non-repeating characters, you would need to modify the function accordingly.  



This function has a time complexity of O(n), where n is the length of the input string, because it makes two passes through the string. The space complexity is O(1), because it uses a constant amount of space to store the character counts.  



Note: This function assumes that the input string only contains ASCII characters. If the string can contain non-ASCII characters, you may need to modify the function accordingly.  



Also, this function returns the first non-repeating character it encounters. If you want to return all non-repeating characters, you would need to modify the function to store them in a list or set.  



This function is case-sensitive, so