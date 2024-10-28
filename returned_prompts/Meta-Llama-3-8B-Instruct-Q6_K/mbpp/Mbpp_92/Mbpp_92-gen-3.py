The problem is asking to write a function that checks whether a given number is undulating or not. A number is considered undulating if it contains at least one pair of consecutive digits that are different.

From the given unit test `assert is_undulating(1212121) == True`, we can infer that the number 1212121 is undulating because it has consecutive pairs of different digits (12, 21, 12, etc.).

Here is a Python function that solves the problem:
```
def is_undulating(n):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] != n[i+1]:
            return True
    return False
```
This function converts the given number to a string and then checks each pair of consecutive digits. If it finds a pair that is different, it returns True, indicating that the number is undulating. If it doesn't find any such pair, it returns False, indicating that the number is not undulating. 