

def fib(n: int):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)

# Tests:
print(fib(10))
print(fib(1))
print(fib(8))

# This solution works, but it's not efficient. It has a time complexity of O(2^n) because it solves the same subproblems over and over again.
# A better approach would be to use dynamic programming to store the results of the subproblems and use them to solve the larger problems.

# This function calculates the fibonacci series using Dynamic Programming:


def fib_dp(n: int):
    fib_values = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib_values[i] = fib_values[i - 1] + fib_values[i - 2]
    return fib_values[n]


# Tests:
print(fib_dp(10))
print(fib_dp(1))
print(fib_dp(8))
<jupyter_output>
55
1
21
55
1
21
<jupyter_text>
Problem 2: Find the longest common substring between two strings.
<jupyter_code>
