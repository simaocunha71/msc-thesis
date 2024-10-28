```
def number_ctr(s):
    return sum(c.isdigit() for c in s)
```





In this problem, we need to write a python function that counts the number of digits in a given string. The function should return the count of digits in the string. 

For example, if the input string is 'program2bedone', the function should return 1 because there is only one digit '2' in the string.

The unit test provided is `assert number_ctr('program2bedone') == 1`, which checks if the function correctly counts the number of digits in the given string.

Here is the solution for the problem:
```
def number_ctr(s):
    return sum(c.isdigit() for c in s)
```
In this solution, we use a generator expression to iterate over each character `c` in the string `s`. The `isdigit()` method returns `True` if the character is a digit and `False` otherwise. We use the `sum` function to count the number of `True` values, which corresponds to the number of digits in the string.