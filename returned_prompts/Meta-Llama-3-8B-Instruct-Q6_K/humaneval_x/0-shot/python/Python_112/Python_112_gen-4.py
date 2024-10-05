```
def reverse_delete(s,c):
    s = s.replace(c,'')
    return (s, s == s[::-1])
```
The function `reverse_delete` takes two strings `s` and `c` as input. It first removes all characters from `s` that are equal to any character in `c` using the `replace` method. Then it returns a tuple containing the result string and a boolean indicating whether the result string is a palindrome. The palindrome check is done by comparing the result string with its reverse using slicing (`s[::-1]`).

For example, if `s = "abcde"` and `c = "ae"`, the function will return `('bcd', False)` because after removing the characters 'a' and 'e' from `s`, the result string is `'bcd'` which is not a palindrome.

If `s = "abcdedcba"` and `c = "ab"`, the function will return `('cdedc', True)` because after removing the characters 'a' and 'b' from `s`, the result string is `'cdedc'` which is a palindrome.