def highest_Power_of_2(n):
    result = 1
    while n > result:
        result *= 2
    return result