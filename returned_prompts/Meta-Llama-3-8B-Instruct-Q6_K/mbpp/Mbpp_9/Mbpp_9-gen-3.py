```
def find_Rotations(s):
    n = len(s)
    for i in range(1, n):
        if s == s[i:] + s[:i]:
            return i
    return n
```


This function works by iterating over the string and checking if the string is equal to itself rotated by i positions. If it is, it returns i. If it's not after checking all positions, it returns the length of the string, which means that the string is already the same after rotation.

For example, for the string "aaaa", the function will return 1, because the string "aaaa" is equal to itself rotated by 1 position. For the string "abcde", the function will return 5, because the string "abcde" is equal to itself rotated by 5 positions. If the string is "abcdeabcde", the function will return 5, because the string "abcdeabcde" is equal to itself rotated by 5 positions. If the string is "abc", the function will return 3, because the string "abc" is equal to itself rotated by 3 positions. If the string is "a", the function will return 1, because the string "a" is equal to itself rotated by 1 position. If the string is "abcabc", the function will return 3, because the string "abcabc" is equal to itself rotated by 3 positions. If the string is "abcabcabc", the function will return 3, because the string "abcabcabc" is equal to itself rotated by 3 positions. If the string is "abcabcabcabc", the function will return 4, because the string "abcabcabcabc" is equal to itself rotated by 4 positions. If the string is "abcabcabcabcabc", the function will return 5, because the string "abcabcabcabcabc" is equal to itself rotated by 5 positions. If the string is "abcabcabcabcabcabc", the function will return 6, because the string "abcabcabcabcabcabc" is equal to itself rotated by 6 positions. If the string is "abcabcabcabcabcabcabc", the function will return 7, because the string "abcabcabcabcabcabcabc" is equal to itself rotated by 7 positions. If the string is "abcabcabcabcabcabcabcabc", the function will return 8, because the string "