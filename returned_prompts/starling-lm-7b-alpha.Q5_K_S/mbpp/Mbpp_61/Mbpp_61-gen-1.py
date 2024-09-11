```
def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if len(str(int(s[i:j]) + int(s[i:j]))) == j - i:
                count += 1
    return count
```

# Here is the explanation of the above code:

The function `count_Substrings` takes a string `s` as an input and returns the number of substrings with the sum of digits equal to their length.

We initialize a variable `count` to keep track of the count of such substrings. We also calculate the length of the input string `s` and store it in the variable `n`.

Next, we use two nested loops to iterate through all possible substrings of the input string `s`. The outer loop iterates from the first character of the string to the second-last character. The inner loop iterates from the current outer loop index to the end of the string.

Inside the inner loop, we convert the substring from the outer loop index to the inner loop index to an integer and add it to itself. Then, we convert the result back to a string and calculate its length using the `len` function.

If the length of the resulting string is equal to the length of the substring (i.e., `j - i`), we increment the `count` variable by 1.

Finally, we return the total count of substrings with the sum of digits equal to their length.

To test the function, you can use the `assert` statement to compare the result of `count_Substrings` with the expected output for a given input. In this case, the expected output for the input `'112112'` is `6`.

```python
assert count_Substrings('112112') == 6
```

This assertion will pass if the function `count_Substrings` returns `6` for the input `'112112'`, indicating that the function is correctly counting the number of substrings with the sum of digits equal to their length.

```python
def count_Substrings