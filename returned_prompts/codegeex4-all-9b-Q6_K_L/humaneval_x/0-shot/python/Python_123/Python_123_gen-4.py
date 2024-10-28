def get_odd_collatz(n):
    collatz = []
    while n > 1:
        collatz.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    collatz.append(1)
    return sorted([i for i in collatz if i % 2 != 0])

print(get_odd_collatz(5)) # [1, 5]
print(get_odd_collatz(10)) # [5, 9]
print(get_odd_collatz(100)) # [3, 5, 9, 33, 17, 13, 41, 61, 97]
print(get_odd_collatz(1000)) # [5, 9, 17, 33, 65, 25, 19, 73, 137, 413, 241, 721, 215, 323, 969]