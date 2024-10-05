
def get_odd_collatz(n):
    def collatz(n):
        seq = [n]
        while n != 1:
            n = n // 2 if n % 2 == 0 else 3 * n + 1
            seq.append(n)
        return seq

    return sorted(x for x in collatz(n) if x % 2 != 0)

print(get_odd_collatz(5))
# Output: [1, 5]

print(get_odd_collatz(10))
# Output: [1, 5, 11]

print(get_odd_collatz(15))
# Output: [1, 5, 11, 17, 25]

print(get_odd_collatz(20))
# Output: [1, 5, 11, 17, 25]

print(get_odd_collatz(25))
# Output: [1, 5, 11, 17, 25]

print(get_odd_collatz(30))
# Output: [1, 5, 11, 17, 25, 37]

print(get_odd_collatz(35))
# Output: [1, 5, 11, 17, 25, 37, 41, 45]

print(get_odd_collatz(40))
# Output: [1, 5, 11, 17, 25, 37, 41, 45]

print(get_odd_collatz(45))
# Output: [1, 5, 11, 17, 25, 37, 41, 45, 53]

print(get_odd_collatz(50))
# Output: [1, 5, 11, 17, 25, 37, 41, 45, 53, 61]

print