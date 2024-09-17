def is_Sum_Of_Powers_Of_Two(n):
    # Check if the number is negative
    if n < 0:
        return False

    # Check if the number is a power of 2
    while n % 2 == 0:
        n //= 2

    # If the number is a power of 2, it can't be represented as the sum of non-zero powers of 2
    if n == 1:
        return False

    # Otherwise, try to find a representation
    for i in range(n.bit_length(), 0, -1):
        # Check if the number is divisible by 2^i
        if n % (2 ** i) == 0:
            # If it is, subtract 2^i from the number and continue
            n -= 2 ** i

    # If the number is now 0, it can be represented as the sum of non-zero powers of 2
    return n == 0