You can solve this problem by iterating through the string and keeping track of the maximum run of uppercase characters. Here's a Python solution:

```python
def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for char in s:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run
```

This function iterates through the string `s` and checks each character if it's uppercase using the `isupper()` method. If the character is uppercase, it increments the `current_run` variable and updates the `max_run` variable if necessary. If the character is not uppercase, it resets the `current_run` variable to 0. Finally, it returns the maximum run of uppercase characters found in the string. The unit test `assert max_run_uppercase('GeMKSForGERksISBESt') == 5` ensures that the function works correctly for a given string.