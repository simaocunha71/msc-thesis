def is_Sum_Of_Powers_Of_Two(n):
    # If n is 0 or 1, it can be represented as the sum of non-zero powers of 2
    if n == 0 or n == 1:
        return True
    # If n is odd, it cannot be represented as the sum of non-zero powers of 2
    if n % 2 != 0:
        return False
    # If n is even, check whether n-1 can be represented as the sum of non-zero powers of 2
    return is_Sum_Of_Powers_Of_Two(n // 2 - 1)