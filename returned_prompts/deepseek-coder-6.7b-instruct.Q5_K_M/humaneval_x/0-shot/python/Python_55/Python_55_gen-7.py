

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

# Using dynamic programming to store the previously computed values
# This reduces the time complexity from exponential to linear
def fib_dp(n: int):
    fib_values = [0, 1]
    for i in range(2, n + 1):
        fib_values.append(fib_values[i - 1] + fib_values[i - 2])
    return fib_values[n]

print(fib_dp(10))
print(fib_dp(1))
print(fib_dp(8))

# This is the best solution as it uses the formula for Fibonacci numbers which has a time complexity of O(log n)
def fib_formula(n: int):
    phi = (1 + 5 ** 0.5) / 2
    return int(phi ** n / 5 ** 0.5 + 0.5)

print(fib_formula(10))
print(fib_formula(1))
print(fib_formula(8))

# This solution is efficient as it uses the properties of Fibonacci numbers
def fib_matrix(n: int):
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]

def multiply(F, M):
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[