

def fib(n: int):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))
print(fib(1))
print(fib(8))


# The above program uses recursion to calculate the nth Fibonacci number.
# However, the time complexity of this program is O(2^n) as each function call branches into two new function calls.
# To improve the time complexity, we can use memoization where we store the results of expensive function calls and reuse them in future function calls.

def fib(n: int, memo={}):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(10))
print(fib(1))
print(fib(8))


# The above program now has a time complexity of O(n), making it much faster for larger inputs.

# The space complexity of this program is O(n) as it uses a dictionary to store the results of the function calls.
# This can be reduced to O(1) by only storing the last two results of the Fibonacci sequence.

def fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fib(10))
print(fib(1))
print(fib(8))


# The above program calculates the nth Fibonacci number in O(n) time and O(1) space.
<jupyter_output>
55
1
21
55
1
21
55
1
21
<jupyter_text>
Problem 2: Find the missing number in an array