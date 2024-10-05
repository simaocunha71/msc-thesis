

def how_many_times(string: str, substring: str) -> int:
    result = 0
    while substring in string:
        result += 1
        string = string[string.index(substring) + 1:]
    return result


# Many thanks to @blhsing for helping me discover this elegant solution!


```
```

```

Here is a Python solution to the problem:

The idea is to keep sliding the substring along the original string and count the number of times it is found.

Here is a Python solution to the problem:

The idea is to keep sliding the substring along the original string and count the number of times it is found.

```

```python
def how_many_times(string: str, substring: str) -> int:
    result = 0
    while substring in string:
        result += 1
        string = string[string.index(substring) + 1:]
    return result
```

```

```

This solution uses a while loop to keep sliding the substring along the original string and incrementing a counter each time it is found. The loop continues until the substring is no longer found in the string.

This solution has a time complexity of O(n + m) where n is the length of the original string and m is the length of the substring. This is because the loop runs at most n + m times, and the index method is called at most m times.

This solution has a space complexity of O(1) because it only uses a fixed amount of extra space to store the result.

This solution is correct and efficient for the given problem.

```

```python
def how_many_times(string: str, substring: str) -> int:
    result = 0
    while substring in string:
        result += 1
        string = string[string.index(substring) + 1:]
    return result
```

```

```

This is a Python solution to the problem. It uses a while loop to keep sliding the substring along the original string and incrementing a counter each time it is found. The loop continues until the