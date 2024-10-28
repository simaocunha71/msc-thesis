```
def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None
```


This function iterates over the input string and checks if each character is in the set. If a character is found in the set, it means that it has been seen before, so the function returns that character. If the function finishes iterating over the string without finding a repeated character, it returns None. The unit test `assert first_repeated_char("abcabc") == "a"` ensures that the function returns the first repeated character in the string. 

The time complexity of this function is O(n) and the space complexity is O(n) where n is the length of the input string. This is because the function uses a set to store the characters it has seen, and the size of the set is proportional to the length of the input string. 