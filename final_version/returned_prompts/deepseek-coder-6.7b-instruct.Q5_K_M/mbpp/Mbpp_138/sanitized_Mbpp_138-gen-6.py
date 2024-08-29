def is_Sum_Of_Powers_Of_Two(n):
    # base case
    if n == 0:
        return False
    if n == 1:
        return True
    # recursive case
    return any(is_Sum_Of_Powers_Of_Two(n - 2**i) for i in range(31))