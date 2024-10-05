
```python
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count
```

This function works by starting from the beginning of the string and repeatedly searching for the substring. When it finds one, it increments the count and moves the start position one character after the found substring. If it doesn't find any more substrings, it breaks out of the loop and returns the count.

This function also counts overlaping cases, as it starts searching from the character immediately after the last found substring.

It's also worth noting that the find method in python returns -1 when it can't find the substring in the string, which allows us to break out of the loop when there are no more substrings to be found.

This solution is efficient because it only scans the string once, making it a O(n) time complexity solution.

It's also worth noting that this function is case sensitive, so 'aa' and 'AA' would be counted as different substrings.

You can use this function in your code as follows:

```python
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This will print the number of times the substring 'aa' can be found in the string 'aaaa'.

The function is also very flexible and can be used with any string and substring.

For example:

```python
print(how_many_times('bananas', 'na'))  # Output: 2
```

This will print the number of times the substring 'na' can be found in the string 'bananas'.

As you can see, this function works very well and is very useful for string manipulation tasks in Python.































































