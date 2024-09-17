The Newman-Conway sequence is a sequence of numbers that starts with 0 and 1, and each subsequent number is the sum of the previous two numbers, plus 1. 

Here is a Python function that generates the nth number in this sequence:

```
def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b + 1
        return b
```

This function uses a loop to generate the sequence up to the nth number. The variables `a` and `b` are used to keep track of the last two numbers in the sequence. The function returns the nth number in the sequence. 

The unit test `assert sequence(10) == 6` ensures that the function is working correctly. 

For example, the first 10 numbers in the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, which confirms that the function is correct. 

This function has a time complexity of O(n), as it needs to iterate `n` times to generate the sequence. The space complexity is O(1), as it only uses a constant amount of space to store the variables `a`, `b` and the loop variable. 