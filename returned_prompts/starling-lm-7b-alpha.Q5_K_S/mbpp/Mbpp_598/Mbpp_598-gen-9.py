
def armstrong_number(n):
    sum_of_cubes = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    if sum_of_cubes == n:
        return True
    return False


