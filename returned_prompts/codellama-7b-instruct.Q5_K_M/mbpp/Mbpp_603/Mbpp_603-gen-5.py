def get_lucid_numbers(n):
    lucid_numbers = []
    for i in range(1, n+1):
        if is_lucid_number(i):
            lucid_numbers.append(i)
    return lucid_numbers

def is_lucid_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


