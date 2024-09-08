Here is the Python function for the problem:

```python
def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for char in s:
        if char.isupper():
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 0
    return max_run

print(max_run_uppercase('GeMKSForGERksISBESt'))  # Outputs: 5
```

In this function, we iterate through the string `s`. For each character, we check if it is uppercase by using the `isupper()` method. If it is uppercase, we increase the `current_run` count. If `current_run` is greater than `max_run` at any point, we update `max_run` with `current_run`. If the character is not uppercase, we reset `current_run` to 0. The function finally returns the maximum run of uppercase characters in `s`.

This function works by checking each character in the string and keeping track of the current run of uppercase characters and the maximum run found so far. It does this by iterating over each character in the string and updating the count if it is uppercase, and resetting the count if it is not.
"""

