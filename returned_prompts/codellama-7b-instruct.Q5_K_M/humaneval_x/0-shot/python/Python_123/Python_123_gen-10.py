
def get_odd_collatz(n):
    odd_numbers = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        odd_numbers.append(n)
    return sorted(odd_numbers)
