def armstrong_number(n):
    temp = n
    sum = 0
    power = len(str(n))
    while n > 0:
        digit = n % 10
        sum += digit ** power
        n //= 10
    return sum == temp