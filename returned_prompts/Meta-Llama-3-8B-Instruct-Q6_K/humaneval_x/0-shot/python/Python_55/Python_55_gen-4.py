```
def fib(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
```



Explanation:
This function calculates the n-th Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

The function first checks if n is less than or equal to 0, and if so, raises a ValueError with the message "n must be a positive integer".

If n is 1 or 2, the function returns 1, as these are the first two numbers in the Fibonacci sequence.

For n greater than 2, the function initializes two variables a and b to 1, and then enters a loop that runs n-2 times. In each iteration of the loop, the values of a and b are updated to be b and a+b, respectively. This effectively calculates the n-th Fibonacci number.

Finally, the function returns the value of b, which is the n-th Fibonacci number.

The time complexity of this function is O(n), as it needs to iterate n-2 times to calculate the n-th Fibonacci number. The space complexity is O(1), as it only uses a constant amount of space to store the values of a and b.