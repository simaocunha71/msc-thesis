```
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


This function iterates over the string, and for each character, it checks if it is uppercase. If it is, it increments the current run length and updates the maximum run length if necessary. If the character is not uppercase, it resets the current run length to 0. Finally, it returns the maximum run length. The unit test `assert max_run_uppercase('GeMKSForGERksISBESt') == 5` confirms that the function works correctly.