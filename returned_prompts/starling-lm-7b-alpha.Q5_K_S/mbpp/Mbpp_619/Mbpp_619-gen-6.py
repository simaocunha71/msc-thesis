Here is a Python program to solve this problem:

```python
def move_num(s):
    numbers = []
    for c in s:
        if c.isdigit():
            numbers.append(c)
    for c in numbers:
        s = s.replace(c, '')
    return s + ''.join(numbers)
```

Explanation:
This function `move_num` takes a string `s` as an argument and returns a new string with all the numbers moved to the end of the string. 

The function first initializes an empty list called `numbers`. Then, it loops through each character `c` in the input string `s`. If the character `c` is a digit, it is appended to the `numbers` list. 

After that, the function loops through each character in the `numbers` list and replaces each character in the original string `s` with an empty string using the `replace` method. This effectively removes all the numbers from the original string. 

Finally, the function concatenates the modified string `s` with the `numbers` list joined together using the `join` method and returns the result. 

The provided assertion in the problem statement checks if the `move_num` function correctly moves all the numbers to the end of the given string. 

For example, if we call `move_num('I1love143you55three3000thousand')`, the function will return `'Iloveyouthreethousand1143553000'`, which is the expected result.
```

```

```

```python

```

```

```

```python

```

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

```

```python

```

```python

```

```python

```

```python

```

``