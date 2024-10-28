

def fib4(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    fib = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4])
    return fib[n]


print(fib4(5))
print(fib4(6))
print(fib4(7))
"""
Output:
4
8
14
"""


def fib4(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    a, b, c, d = 0, 0, 2, 0
    for _ in range(n - 3):
        a, b, c, d = b, c, d, a + b + c + d
    return d


print(fib4(5))
print(fib4(6))
print(fib4(7))
"""
Output:
4
8
14
"""

"""
The second solution is more efficient than the first one because it only keeps the last four numbers in the sequence instead of all numbers. This means that it uses less memory and is faster.
"""

"""
The time complexity of the solution is O(n) and the space complexity is O(1) because it only keeps the last four numbers in the sequence.
"""

"""
This solution works by initializing the first four numbers of the sequence. Then, it iteratively calculates the next number in the sequence by summing the last four numbers. This is done n - 3 times because the first four numbers are already initialized. Finally, it returns the n-th number in the sequence.
"""

"""
This solution is based on the definition of the fib4 sequence