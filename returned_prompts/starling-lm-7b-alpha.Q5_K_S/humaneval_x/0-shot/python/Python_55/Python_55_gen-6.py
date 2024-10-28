
To solve this problem, we can use a dynamic programming approach to store the Fibonacci numbers we have already computed. Here's the code:

```python
def fib(n: int):
    # Base case: Fibonacci number at index 0 and 1 is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Initialize the array with infinite values
    else:
        fib_num = [0 for _ in range(n + 1)]
        # Calculate the Fibonacci numbers
        fib_num[0] = 0
        fib_num[1] = 1
        # Calculate the Fibonacci numbers from index 2 to n
        for i in range(2, n + 1):
            fib_num[i] = fib_num[i - 1] + fib_num[i - 2]
        return fib_num[n]
```

In this code, we first check for the base cases where the Fibonacci number at index 0 and 1 is 1. Then, we initialize a list called `fib_num` with the length `n + 1`, and set all the values to 0. This list will store the Fibonacci numbers we have already computed.

Next, we calculate the Fibonacci numbers at index 0 and 1, which are 0 and 1 respectively. Then, we use a loop to calculate the Fibonacci numbers from index 2 to `n`. In each iteration of the loop, we add the two previous Fibonacci numbers (`fib_num[i - 1]` and `fib_num[i - 2]`) and store the result in `fib_num[i]`. Finally, we return the Fibonacci number at index `n`.

This implementation has a time complexity of O(n) and a space complexity of O(n).

You can test the function with the provided examples:

```python
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
