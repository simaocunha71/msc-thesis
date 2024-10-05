

def fib(n: int):
    fib_numbers = [0, 1]
    while len(fib_numbers) < n + 1:
        fib_numbers.append(0)
    if n <= 1:
        return n
    else:
        if fib_numbers[n - 1] == 0:
            fib_numbers[n - 1] = fib(n - 1)
        if fib_numbers[n - 2] == 0:
            fib_numbers[n - 2] = fib(n - 2)
    fib_numbers[n] = fib_numbers[n - 2] + fib_numbers[n - 1]
    return fib_numbers[n]


print(fib(10))
print(fib(1))
print(fib(8))


The function uses memoization to store already computed Fibonacci numbers. This way, when the function needs to calculate a Fibonacci number that it has already calculated before, it can use this stored number instead of recalculating it. This significantly speeds up the function for larger inputs.


This function also uses a dynamic programming approach to build up the Fibonacci sequence. It first initializes a list of size n+1 with the first two Fibonacci numbers (0 and 1). It then fills up the rest of the list by summing up the two previous numbers. This approach is more efficient than the recursive approach because it avoids the need to recalculate the same Fibonacci numbers multiple times.
'''

# Solution 2:

'''
The function uses a bottom-up dynamic programming approach. It starts by initializing the first two Fibonacci numbers, then iteratively calculates the next Fibonacci numbers based on the previous two. This approach is more efficient than the previous one because it avoids the need to recalculate the same Fibonacci numbers multiple times.
'''

# Solution 3:

'''
The function uses a bottom-up dynamic programming approach. It starts by initializing the first two Fibonacci numbers, then iteratively calculates the next F