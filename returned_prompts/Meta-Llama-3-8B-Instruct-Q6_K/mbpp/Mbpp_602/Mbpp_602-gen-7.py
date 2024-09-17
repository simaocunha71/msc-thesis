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
The function first counts the occurrence of each character in the string. Then it iterates over the string again to find the first character that has a count greater than 1.

The unit test `assert first_repeated_char("abcabc") == "a"` ensures that the function works correctly. It checks that the function returns "a" when given the input "abcabc", which is the first repeated character in the string.  If the function returns None when there is no repeated character, it will pass the test as well.  



This function has a time complexity of O(n), where n is the length of the input string, because it iterates over the string twice. The space complexity is O(1), because it uses a constant amount of space to store the character count dictionary.  



This function can be further optimized by using a dictionary to store the characters and their counts, which would reduce the time complexity to O(n) for both the counting and the searching. The optimized function would look like this:
```
def first_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            return char
    return None
```
This function still has a time complexity of O(n), but it uses less space because it only stores the characters that have been seen so far, rather than storing all the characters in the string.  



The function can also be optimized by using a set to store the characters that have been seen so far, which would reduce the time complexity to O(n) for both the counting and the searching. The optimized function would look like this:
```
def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None
```
This function still has a time complexity of O(n), but it uses less space because it only stores the characters that have been seen so