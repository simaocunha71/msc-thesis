
The Fibonacci sequence is defined by the following recurrence relation: $F_n = F_{n-1} + F_{n-2}$. Given a number $n$, the Fibonacci number $F_n$ is the result of the Fibonacci sequence at index $n$.

The Fibonacci numbers are defined as follows:

- $F_0 = 0$
- $F_1 = 1$
- $F_n = F_{n-1} + F_{n-2}$ for $n \ge 2$

To calculate the Fibonacci number at index $n$, we can use the following algorithm:

1. Initialize a list of the first two Fibonacci numbers: `fib = [0, 1]`
2. Iterate from 2 to $n$:
   - Calculate the next Fibonacci number: $F_n = F_{n-1} + F_{n-2}$
   - Add the calculated Fibonacci number to the list: `fib.append(F_n)`
3. Return the Fibonacci number at index $n$: `return fib[n]`

In Python, we can implement this algorithm as follows:

```python
def fib(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
```

Here are some test cases to verify the correctness of the implementation:

```python
print(fib(10))  # 55
print(fib(1))   # 1
print(fib(8))   # 21
```

The output of these test cases matches the expected results.

The time complexity of this algorithm is $O(n)$ because we iterate from 2 to $n$ to calculate the Fibonacci numbers. The space complexity is also $O(n)$ because we store all the Fibonacci numbers in a list.

This algorithm has a relatively low time complexity compared to other algorithms for calculating Fibonacci numbers, such as recursion or matrix exponentiation.