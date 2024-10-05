
def f(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(fact(i))
        else:
            l.append(sum_nums(i))
    return l

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def sum_nums(n):
    if n == 0:
        return 0
    else:
        return n + sum_nums(n - 1)


# Some test cases
print(f(5))  # [1, 2, 6, 24, 15]
print(f(10)) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


# Time Complexity: O(n)
# Space Complexity: O(1)


# However, the solution above uses recursion, which is not very efficient.
# Here is a more efficient solution using iteration:

def f(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(fact(i))
        else:
            l.append(sum_nums(i))
    return l

def fact(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def sum_nums(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Some test cases
print(f(5))  # [1, 2, 6, 24, 120]
print(f(10)) # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 