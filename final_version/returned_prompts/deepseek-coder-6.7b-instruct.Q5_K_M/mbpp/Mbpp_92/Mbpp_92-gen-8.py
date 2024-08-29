"""
An undulating number is a number in which the adjacent digits differ by 2 and the sequence repeats.

For example, 1212121 is an undulating number because:
    1 and 2 diff by 2
    2 and 1 diff by 1
    1 and 2 diff by 2
    2 and 1 diff by 1
    1 and 2 diff by 2
    2 and 1 diff by 1
    1 and 2 diff by 2
And the sequence repeats.

So, we will use a loop to check each digit and its next digit, and the difference should be 2.
We also need to check whether the sequence repeats or not.

Here is the Python code:
"""

def is_undulating(n):
    s = str(n)
    if len(s) < 3:
        return False
    diff = abs(int(s[0]) - int(s[1]))
    if diff != 2:
        return False
    for i in range(1, len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) != 2:
            return False
    return True

print(is_undulating(1212121))  # should return True

"""
In the above code, we first convert the number to a string. Then we check the length of the string. If it's less than 3, we return False because a number with less than 3 digits cannot be undulating. Then we calculate the difference between the first two digits. If the difference is not 2, we return False. We then loop through the rest of the digits in the string, checking the difference between each pair of digits. If any pair of digits do not have a difference of 2, we return False. If we get through all these checks without returning False, we return True, indicating that the number is undulating.
"""

```

## Code Snippet 2:

```python

