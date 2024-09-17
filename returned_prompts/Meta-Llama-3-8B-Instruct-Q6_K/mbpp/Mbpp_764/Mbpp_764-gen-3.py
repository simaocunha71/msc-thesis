```
def number_ctr(s):
    return sum(c.isdigit() for c in s)
```


Explanation:
This function uses a generator expression to iterate over each character in the input string. The `isdigit()` method checks if a character is a digit, and the `sum()` function counts the number of True values (i.e., the number of digits) in the string. The function name `number_ctr` is chosen to match the problem's requirement.

The unit test `assert number_ctr('program2bedone') == 1` ensures that the function correctly counts the single digit '2' in the input string. The function works for strings containing multiple digits, as well as strings containing no digits at all.