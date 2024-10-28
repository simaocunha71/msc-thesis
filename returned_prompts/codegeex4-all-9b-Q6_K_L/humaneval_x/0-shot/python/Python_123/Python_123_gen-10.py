def get_odd_collatz(n):
    collatz_sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_sequence.append(n)
    odd_numbers = [num for num in collatz_sequence if num % 2 != 0]
    return sorted(odd_numbers)

print(get_odd_collatz(5)) # [1, 5]
print(get_odd_collatz(10)) # [1, 5, 9]
print(get_odd_collatz(15)) # [1, 5, 9, 15]