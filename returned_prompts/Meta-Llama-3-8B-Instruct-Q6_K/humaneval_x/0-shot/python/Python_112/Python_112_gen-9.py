```
def reverse_delete(s,c):
    new_s = [char for char in s if char not in c]
    return (''.join(new_s), new_s == new_s[::-1])
```


The task is to create a function that takes two strings, `s` and `c`, and returns a tuple containing the result string and a boolean value indicating whether the result string is a palindrome.

The function should delete all characters in `s` that are equal to any character in `c`, and then check if the result string is a palindrome. If it is, the function should return `True`; otherwise, it should return `False`.

Here is a Python solution that achieves this:

```python
def reverse_delete(s,c):
    new_s = [char for char in s if char not in c]
    return (''.join(new_s), new_s == new_s[::-1])
```

This function uses a list comprehension to create a new list `new_s` that contains only the characters from `s` that are not in `c`. It then joins this list into a string using the `join` method and returns a tuple containing this string and a boolean value indicating whether the string is a palindrome.

The boolean value is determined by comparing the string with its reverse using slicing (`new_s[::-1]`). If the string is equal to its reverse, it is a palindrome, and the function returns `True`. Otherwise, it returns `False`.