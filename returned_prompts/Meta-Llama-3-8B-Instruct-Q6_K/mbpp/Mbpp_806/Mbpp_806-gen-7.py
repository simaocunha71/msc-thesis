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
The function `max_run_uppercase` takes a string `s` as input and returns the maximum run of uppercase characters in the string. It initializes two variables: `max_run` to keep track of the maximum run found so far and `current_run` to keep track of the current run of uppercase characters. It then iterates over each character in the string. If the character is uppercase, it increments `current_run`. If the character is lowercase, it updates `max_run` with the maximum of `max_run` and `current_run`, and then resets `current_run` to 0. Finally, it returns the maximum of `max_run` and `current_run` to handle the case where the string ends with a run of uppercase characters. The unit test `assert max_run_uppercase('GeMKSForGERksISBESt') == 5` ensures that the function works correctly. 





The time complexity of this function is O(n), where n is the length of the string, as it needs to iterate over each character in the string once. The space complexity is O(1), as it only uses a constant amount of space to store the variables.