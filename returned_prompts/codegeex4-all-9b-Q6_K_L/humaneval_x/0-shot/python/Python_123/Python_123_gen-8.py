def get_odd_collatz(n):
    collatz = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        collatz.append(n)
    return sorted([i for i in collatz if i % 2 == 1])

print(get_odd_collatz(5))
print(get_odd_collatz(10))
print(get_odd_collatz(15))
print(get_odd_collatz(20))
print(get_odd_collatz(1))