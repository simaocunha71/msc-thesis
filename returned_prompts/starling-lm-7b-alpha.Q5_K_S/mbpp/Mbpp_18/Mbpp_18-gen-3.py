```
def remove_dirty_chars(string1, string2):
    for i in string2:
        while i in string1:
            string1 = string1.replace(i, "")
    return string1
```

In the above code, we define a function `remove_dirty_chars` that takes two strings as input parameters. We then iterate through each character in the second string and while it is present in the first string, we remove it using the `replace` function. Finally, we return the modified first string.

To test the function, we use the `assert` statement to check if the expected output is `'bacuve'` when we pass the strings `'probasscurve'` and `'pros'` as arguments to the function.

This solution will remove all occurrences of the characters in the second string from the first string.

```python
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
```

This assertion will pass if the `remove_dirty_chars` function correctly removes the characters from the first string that are present in the second string.

```
Output:
True
```

The output will be `True` if the assertion passes, indicating that the function is working correctly.

```
Explanation:
In the provided solution, we define a function `remove_dirty_chars` that takes two strings as input parameters. We then iterate through each character in the second string using a `for` loop. Inside the loop, we use a `while` loop to check if the current character is present in the first string. If it is, we remove all occurrences of that character from the first string using the `replace` function. Finally, we return the modified first string.

To test the function, we use the `assert` statement to check if the expected output is `'bacuve'` when we pass the strings `'probasscurve'` and `'pros'` as arguments to the function. This assertion will pass if the `remove_dirty_chars` function correctly removes the characters from the first string that are present in the second string, and the output is `'bacuve'`.
```

Note: This solution assumes that