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


Explanation:
The function `max_run_uppercase` takes a string `s` as input and returns the maximum run of uppercase characters in the string.

It initializes `max_run` to 0, which will store the maximum run of uppercase characters, and `current_run` to 0, which will store the current run of uppercase characters.

It iterates over each character in the string. If the character is uppercase (checked using the `isupper` method), it increments `current_run` and updates `max_run` if `current_run` is greater than `max_run`. If the character is not uppercase, it resets `current_run` to 0.

Finally, it returns `max_run`, which is the maximum run of uppercase characters in the string.

The unit test `assert max_run_uppercase('GeMKSForGERksISBESt') == 5` ensures that the function is working correctly, as the maximum run of uppercase characters in the string 'GeMKSForGERksISBESt' is indeed 5.