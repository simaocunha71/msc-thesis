
The Fibonacci sequence is a series of numbers in which each number after the first two is the sum of the two preceding ones. The first ten Fibonacci numbers are:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Here's a function that computes the nth Fibonacci number using dynamic programming, which is a way of solving a problem by breaking it down into simpler subproblems in order to reuse their solutions.

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    fibs = [None] * (n + 1)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]

The function starts by creating a list fibs that will hold the Fibonacci numbers up to the nth number. The first two Fibonacci numbers (0 and 1) are already set in the list. Then it uses a for loop to calculate and store the rest of the Fibonacci numbers in the list. The nth Fibonacci number is the last number in the list, and that's what the function returns.

The function uses a list to store the Fibonacci numbers, which is more efficient than using two variables and repeatedly updating them. By calculating all the Fibonacci numbers up to the nth number, the function can reuse the results of the subproblems, which makes it a good example of dynamic programming.

The time complexity of this function is O(n) because it calculates n Fibonacci numbers, one at a time. The space complexity is also O(n) because it uses a list to store all the Fibonacci numbers up to the nth number.

The function can be used to calculate the nth Fibonacci number for any positive integer n.

