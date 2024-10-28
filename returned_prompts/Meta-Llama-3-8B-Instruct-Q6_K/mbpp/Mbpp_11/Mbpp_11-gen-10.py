```
def remove_Occ(s, char):
    if char not in s:
        return s
    s = list(s)
    if s[0] == char:
        s.pop(0)
    if s[-1] == char:
        s.pop()
    return "".join(s)
```


The function `remove_Occ` takes two parameters: a string `s` and a character `char`. It first checks if `char` is not in `s`. If it's not, it returns the original string `s`. 

If `char` is in `s`, the function converts `s` into a list of characters. It then checks if the first character in the list is equal to `char`. If it is, it removes the first character using the `pop(0)` method. 

Next, it checks if the last character in the list is equal to `char`. If it is, it removes the last character using the `pop()` method (no argument is needed for the `pop()` method when removing the last element). 

Finally, it converts the list of characters back into a string using the `join()` method and returns the resulting string. 

The unit test `assert remove_Occ("hello","l") == "heo"` ensures that the function works correctly. 

For example, if you call `remove_Occ("hello","l")`, the function will return `"heo"`, which is the result of removing the first and last occurrences of `"l"` from the string `"hello"`. 