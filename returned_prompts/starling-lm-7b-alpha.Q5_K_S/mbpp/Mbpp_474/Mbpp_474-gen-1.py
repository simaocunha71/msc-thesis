```python
def replace_char(string, char1, char2):
    new_string = ""
    for c in string:
        if c == char1:
            new_string += char2
        else:
            new_string += c
    return new_string
```

This function `replace_char` takes three parameters: `string`, `char1`, and `char2`. It initializes an empty string `new_string`. Then, it iterates through each character `c` in the input `string`. If `c` is equal to `char1`, it appends `char2` to `new_string`. Otherwise, it appends `c` to `new_string`. Finally, it returns the modified `new_string`.

The provided assertion `assert replace_char("polygon",'y','l')=="pollgon"` tests the function by replacing all occurrences of `'y'` with `'l'` in the string `"polygon"`. The expected result is `"pollgon"`.

The test function `test_replace_char()` runs several test cases to verify the correctness of the `replace_char` function. It asserts that the function returns the expected results for different input combinations. If all tests pass, it prints "All tests passed