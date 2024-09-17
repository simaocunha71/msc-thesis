def get_digit_sum(n):
    return sum(int(digit) for digit in str(n))
def is_lucid(n):
    return get_digit_sum(n) == len([i for i in range(1, n + 1) if n % i == 0])
def get_ludic(n):
    return [i for i in range(1, n + 1) if is_lucid(i)]