```
def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if s[i].lower() == chr(ord('a') + i):
            count += 1
    return count
```


The function `count_char_position(s)` takes a string `s` as input and returns the number of characters in the string that occur at the same position in the string as in the English alphabet (case insensitive). The function iterates over each character in the string and checks if the character (converted to lowercase) is equal to the corresponding character in the English alphabet (also converted to lowercase). If it is, the count is incremented by 1. Finally, the function returns the count. The unit test `assert count_char_position("xbcefg") == 2` ensures that the function works correctly. For example, in the string "xbcefg", the characters 'b' and 'c' occur at the same position in the string as in the English alphabet, so the function returns 2.