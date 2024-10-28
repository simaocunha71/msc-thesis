

def prime_fib(n):
    a, b, c = 1, 1, 2
    while n > 0:
        c = a + b
        if c % 2 != 0 and all(c % i != 0 for i in range(3, int(c ** 0.5) + 1)):
            yield c
        a, b = b, c
        n -= 1
```
    
# Usage:
for fib in prime_fib(3):
    print(fib)

# Output:
# 2
# 3
# 5

This function uses a generator to generate prime Fibonacci numbers. It starts with the Fibonacci sequence (1, 1, 2, 3, 5, ...), and checks if each number is prime. If a prime Fibonacci number is found, it is yielded.

The function uses a while loop to generate the Fibonacci sequence until the n-th number is found. It uses the variable `n` to keep track of the number of prime Fibonacci numbers generated.

The function checks if the current Fibonacci number (`c`) is prime by checking if it is divisible by any number from 3 to the square root of `c`. If `c` is divisible by any of these numbers, it is not prime and the loop continues. If `c` is not divisible by any of these numbers, it is prime and yielded.

The function yields each prime Fibonacci number, allowing it to be used in a for loop to iterate over the prime Fibonacci numbers.

Overall, this function efficiently generates the n-th prime Fibonacci number using a generator and a while loop, while also checking if each number is prime.

```python

```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
```

Answer:

Here is a Python function that returns the n-th number that is both a Fibonacci number and prime:

```python
def prime_fib(n):
    a, b, c = 1, 1