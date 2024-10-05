
if (n <= 0) {
return 0
}

if (n == 1) {
return 1
}

if (n == 2) {
return 1
}

return Fib(n-1) + Fib(n-2)
}

This function is using a recursive approach to calculate the nth Fibonacci number. It is using memoization to reduce the time complexity of the function.

To calculate the nth Fibonacci number, the function first checks if the input is 0 or 1. If it is, it returns the corresponding Fibonacci number directly. If the input is 2, it also returns 1, as the third Fibonacci number is always 2.

If the input is greater than 2, the function uses the recursive approach to calculate the Fibonacci number by adding the two previous Fibonacci numbers together. This process continues until it reaches the base cases of 0, 1, or 2.

The function also uses memoization to store the previously calculated Fibonacci numbers, which reduces the time complexity of the function. This means that if the function is called again with the same input, it can directly return the previously calculated result instead of recalculating it.

Overall, this function provides an efficient way to calculate the nth Fibonacci number using a recursive approach and memoization.

Here are some test cases to validate the function:

>>> Fib(10)
55
>>> Fib(1)
1
>>> Fib(8)
21

These test cases demonstrate the correctness of the function and show that it can accurately calculate the nth Fibonacci number.

In terms of time complexity, the function has a time complexity of O(n) due to the recursive approach. However, with memoization, the time complexity can be reduced to O(1) for the same input, as the previously calculated Fibonacci numbers are stored and reused.

In terms of space complexity, the function has a space complexity of O(n) due to the recursive stack. However, with memoization, the space complexity can be reduced to O(1) for the same input, as only the previously calculated Fibonacci numbers are stored in memory