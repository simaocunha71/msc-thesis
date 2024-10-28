
```python
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count += 1
        else:
            return count
```

This function uses a while loop and the `find` method of the string to find all instances of the substring in the string. The `find` method returns the index of the start of the substring if it is found, otherwise it returns -1. The loop continues until `find` returns -1.

The `start` variable is used as the starting index for the next `find` call. If the substring is found, the `count` variable is incremented, and `start` is set to the index of the next character after the found substring.

The function finally returns the count of all found substrings.

Note: This function does not count overlapping occurrences of the substring. For example, in the string 'aaaa', the substring 'aa' would only be counted once.

Also, this function does not count the occurrences of the substring that is part of another larger substring. For example, in the string 'banana', the substring 'na' would be counted twice, even though 'na' is also part of 'banana'.

If you want to count overlapping occurrences, you will need a slightly different approach.

```python
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while True:
        start = string.find(substring, start)
        if start >= 0:
            count += 1
            start += 1
        else:
            return count
```

In this version, the `start` variable is incremented by 1 after each successful `find` call, so the next `find` call will start searching from the next character. This allows for overlapping occurrences of the substring.



















































