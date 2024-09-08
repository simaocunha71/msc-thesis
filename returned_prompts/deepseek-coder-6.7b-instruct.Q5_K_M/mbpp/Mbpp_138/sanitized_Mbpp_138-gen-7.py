def is_Sum_Of_Powers_Of_Two(n):
    # Base case
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True

    # Initialize starting value to 2^0
    power = 0
    while 2 ** power <= n:
        if is_Sum_Of_Powers_Of_Two(n - 2 ** power):
            return True
        power += 1

    return False