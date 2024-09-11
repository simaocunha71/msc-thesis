Here is one possible way to implement this function:

```python
def occurance_substring(s, substr):
    if substr in s:
        return (substr, s.index(substr), s.index(substr) + len(substr))
    else:
        return None
```

This function first checks if the substring is in the string. If it is, it returns a tuple containing the substring itself, the position of the first occurrence of the substring within the string, and the position of the end of the substring within the string (which is calculated by adding the length of the substring to the position of its beginning). If the substring is not in the string, the function returns None.

The `in` operator is used to check if a substring is in a string. The `index()` method is used to find the position of a substring within a string.

This function can be used as follows:

```python
occurance_substring('python programming, python language','python')
```

It will return `('python', 0, 6)`, which means that the substring 'python' occurs at position 0 in the string 'python programming, python language', and its end is at position 6.

```python
occurance_substring('hello world', 'world')
```

It will return `None`, which means that the substring 'world' does not occur in the string 'hello world'.

This implementation has a time complexity of O(n), where n is the length of the string. This is because we need to check if the substring is in the string and find its position within the string, which both take O(n) time.

This implementation also has a space complexity of O(1), as it only uses a constant amount of extra space to store the result.

Overall, this implementation is quite efficient and should work well for most cases.

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```
```python

```python
```python

```python
``