```
def reverse_delete(s,c):
    for char in set(c):
        s = s.replace(char,'')
    return (s, s == s[::-1])
```


Here's an explanation of the code:

1. `set(c)` converts the string `c` into a set of unique characters. This is done to avoid replacing the same character multiple times.
2. The `for` loop iterates over each character `char` in the set `c`.
3. For each character, the `replace` method is used to replace all occurrences of `char` in `s` with an empty string (`''`). This effectively deletes all occurrences of `char` in `s`.
4. The updated string `s` is then returned as a tuple along with a boolean value indicating whether the resulting string is a palindrome or not. The palindrome check is done by comparing the string `s` with its reverse (`s[::-1]`). If the two strings are equal, then `s` is a palindrome.

Note that this code assumes that the input strings `s` and `c` are ASCII strings. If the input strings can contain non-ASCII characters, additional processing may be required to handle these characters correctly.