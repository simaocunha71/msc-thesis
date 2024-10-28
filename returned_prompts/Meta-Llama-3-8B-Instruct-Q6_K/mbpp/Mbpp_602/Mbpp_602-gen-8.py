```
def first_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] > 1:
            return char
    return None
```



In this function, we first create a dictionary `char_count` to count the frequency of each character in the string. Then we iterate through the string again to find the first character that has a count greater than 1. If no such character is found, the function returns `None`. This function should pass the given unit test. 





The time complexity is O(n), where n is the length of the string, because we are making two passes through the string. The space complexity is also O(n), as in the worst case, all characters in the string are unique, and we need to store all of them in the dictionary.