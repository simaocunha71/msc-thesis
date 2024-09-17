```
def number_ctr(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count
```
This function iterates over each character in the input string. If the character is a digit (checked using the `isdigit()` method), it increments the count. Finally, it returns the count. 

The unit test `assert number_ctr('program2bedone') == 1` ensures that the function correctly counts the single digit in the input string. 





