

def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    a, b, c = 0, 0, 1
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c
    return c


print(fibfib(1))  # 0
print(fibfib(5))  # 4
print(fibfib(8))  # 24


def fibfib_recursive(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib_recursive(n - 1) + fibfib_recursive(n - 2) + fibfib_recursive(n - 3)


print(fibfib_recursive(1))  # 0
print(fibfib_recursive(5))  # 4
print(fibfib_recursive(8))  # 24

# Both functions will output the same result but the first one is much more efficient because it uses a loop instead of recursion.


def fibfib_recursive_memoization(n: int, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        memo[n] = 0
    elif n == 2:
        memo[n] = 1
    else:
        memo[n] = fibfib_recursive_memoization(n - 1, memo) + fibfib_recursive_memoization(n - 2, memo) + fibfib_recursive_memoization(n - 3, memo)
    return memo[n]


print(fibfib_recursive_memoization(1))  # 0
print(fibfib_recursive_memoization(5)) 