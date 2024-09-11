def armstrong_number(n):
    num_digits = len(str(n))
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10
    return sum == n