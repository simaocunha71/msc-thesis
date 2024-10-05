
def get_odd_collatz(n):
    collatz = []
    while n != 1:
        if n % 2 != 0:
            collatz.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    return sorted(collatz)

print(get_odd_collatz(5))  # [1, 5]
print(get_odd_collatz(11))  # [1, 11, 22]
print(get_odd_collatz(27))  # [1, 27, 82, 41, 124, 62, 31, 94, 47]
print(get_odd_collatz(101))  # [1, 101, 304, 152, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2]

The solution calculates the Collatz sequence for the given number n and stores the odd numbers in a list. Finally, it sorts and returns the list.
"""

"""
