def count_Set_Bits(n):
    count = 0
    while n:
        count += n % 2
        n //= 2
    return count