```
def remove_dirty_chars(str1, str2):
    for i in str2:
        str1 = str1.replace(i, '')
    return str1
```
    
    
# Assert
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'

def remove_dirty_chars(str1, str2):
    for i in str2:
        str1 = str1.replace(i, '')
    return str1

# Assert
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'

```
 In the function `remove_dirty_chars`, we're taking two strings as input. We iterate over the second string, and for each character in the second string, we replace the same character in the first string with an empty string. That effectively removes the character from the first string. Then we return the modified first string.

To test the function, we use the `assert` statement to compare the result of `remove_dirty_chars("probasscurve", "pros")` with the expected result of `'bacuve'`. If the two strings are the same, the `assert` statement will pass and the program will continue running. If the two strings are not the same, the `assert` statement will raise an `AssertionError` and the program will stop running.

In this case, the `assert` statement passes because `remove_dirty_chars("probasscurve", "pros")` does indeed return `'bacuve'`.

The `remove_dirty_chars` function can be used to remove characters from the first string which are present in the second string.

```python
def remove_dirty_chars(str1, str2):
    for i in str2:
        str1 = str1.replace(i, '')
    return str1
```
Above is the Python code that defines the `remove_dirty_chars` function. This function takes two strings as input, `str1` and `str2`. It then iterates over each character in `str2` using a for loop. For each character in `str2`, it replaces all occurrences of that character in `str1` with an empty