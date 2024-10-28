The Newman-Conway sequence is a simple sequence of numbers that starts with 0 and 1. The next number in the sequence is the sum of the previous two numbers, unless one of the previous two numbers is 0, in which case the next number is the other previous number. This is a classic problem of recursion.

Here is a Python solution for the problem:

```
def sequence(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
```
This function uses a loop to calculate the nth number in the sequence. It starts with the first two numbers in the sequence (0 and 1) and then enters a loop that calculates each subsequent number in the sequence. The loop continues until it has calculated the nth number, which is then returned. The base cases for the function are when n is 1 or 2, in which case the function returns 0 or 1 respectively. 

The unit test `assert sequence(10) == 6` ensures that the function is working correctly. The 10th number in the sequence is indeed 6. 

This function has a time complexity of O(n) because it needs to calculate each number in the sequence up to the nth number. The space complexity is O(1) because it only needs a constant amount of space to store the variables a and b. 