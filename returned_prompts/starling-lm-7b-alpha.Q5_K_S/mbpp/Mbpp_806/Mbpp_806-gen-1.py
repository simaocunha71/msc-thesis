```
def max_run_uppercase(s):
    max_run = 0
    run = 0
    for i in xrange(len(s)):
        if s[i].isupper():
            run += 1
        else:
            run = 0
        max_run = max(max_run, run)
    return max_run
```

In this implementation, we traverse the string, incrementing the `run` counter if the current character is uppercase, and resetting it if it's not. We also keep track of the maximum `run` we've seen so far. The final result is the `max_run` value.

The time complexity of this solution is O(n), where n is the length of the string, because we visit each character in the string exactly once.

The space complexity is O(1), because we only use a few variables that are independent of the input size.

This solution correctly passes the assertion `assert max_run_uppercase('GeMKSForGERksISBESt') == 5`.

```python
def max_run_uppercase(s):
    max_run = 0
    run = 0
    for i in xrange(len(s)):
        if s[i].isupper():
            run += 1
        else:
            run = 0
        max_run = max(max_run, run)
    return max_run
```

This implementation correctly calculates the maximum run of uppercase characters in the given string.

Here's an example usage of the function:

```python
print(max_run_uppercase('GeMKSForGERksISBESt'))  # Output: 5
```

The function returns the maximum run of uppercase characters, which in this case is 5.

The function works by iterating through the string and keeping track of the current run of uppercase characters and the maximum run seen so far. Whenever a non-uppercase character is encountered, the current run is reset to 0, and the maximum run is updated if necessary.

This solution has a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.

