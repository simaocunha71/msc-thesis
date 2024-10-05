```
def reverse_delete(s,c):
    s = ''.join([i for i in s if i not in c])
    return (s, s == s[::-1])
```


This function works by first using a list comprehension to create a new list of characters that are in the string `s` but not in the string `c`. It then converts this list back into a string and assigns it to the variable `s`. This effectively removes all the characters in `c` from `s`.

The function then returns a tuple containing `s` and a boolean value. The boolean value is `True` if `s` is the same when reversed, and `False` otherwise. This is done using the expression `s == s[::-1]`, which checks if `s` is equal to its reverse.

For example, if `s = "abcde"` and `c = "ae"`, the function would return `('bcd', False)`. If `s = "abcdedcba"` and `c = "ab"`, the function would return `('cdedc', True)`. If `s = "abcdef"` and `c = "b"`, the function would return `('acdef', False)`.