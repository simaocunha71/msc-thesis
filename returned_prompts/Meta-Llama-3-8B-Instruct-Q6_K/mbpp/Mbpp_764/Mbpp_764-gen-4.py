```
def number_ctr(s):
    return sum(c.isdigit() for c in s)
```
The function `number_ctr` takes a string `s` as input and returns the count of digits in the string. It uses a generator expression to iterate over each character `c` in the string, and `c.isdigit()` checks if the character is a digit. The `sum` function then adds up the True/False values (interpreted as 1/0) to give the count of digits. The unit test `assert number_ctr('program2bedone') == 1` ensures that the function correctly counts the single digit '2' in the string. 