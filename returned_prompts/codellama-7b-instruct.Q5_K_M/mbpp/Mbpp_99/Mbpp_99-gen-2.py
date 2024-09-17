
def decimal_to_binary(n):
    if n <= 1:
        return bin(n)
    return decimal_to_binary(n // 2) + str(n % 2)


