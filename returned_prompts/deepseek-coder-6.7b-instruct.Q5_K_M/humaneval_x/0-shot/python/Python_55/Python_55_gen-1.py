

def fib(n: int):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

# print(fib(10))
# print(fib(1))
# print(fib(8))

# The above program is a recursive implementation of Fibonacci series. It works well for small inputs but for larger inputs it can be very slow and inefficient.

# The following is an iterative implementation of Fibonacci series. It is more efficient than the recursive implementation.

def fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib(10))
print(fib(1))
print(fib(8))

# In this program, a and b are two variables that store the last two numbers of the Fibonacci series. For each iteration of the loop, a and b are updated to store the next number of the series. The function returns the nth number of the Fibonacci series.

# The time complexity of this program is O(n), which is much better than the time complexity of the recursive program.

# The space complexity of this program is O(1), which means it uses constant space. This is because it only needs two variables to store the last two numbers of the series, and does not require any additional space that scales with the input size.
<jupyter_output>
<empty_output>
<jupyter_text>
