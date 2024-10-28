```
def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    for char in s:
        if char.isupper():
            current_run += 1
        else:
            max_run = max(max_run, current_run)
            current_run = 0
    return max(max_run, current_run)
```


The function iterates over the given string and checks if each character is uppercase or not. If it is uppercase, it increments the current run. If it is not uppercase, it updates the maximum run if the current run is greater than the maximum run and resets the current run to 0. Finally, it returns the maximum run. If the string ends with an uppercase run, the function returns the maximum run. If the string ends with a lowercase character and the current run is greater than the maximum run, the function returns the current run. Otherwise, it returns the maximum run. The unit test `assert max_run_uppercase('GeMKSForGERksISBESt') == 5` ensures that the function works correctly. For the given string 'GeMKSForGERksISBESt', the function returns 5, which is the maximum run of uppercase characters.