def dif_Square(n):
    # Using the concept of Fermat's Theorem
    # If n can be represented as the difference of two squares
    # then n must be of the form 4^k*(8*m+1)
    # This is because a^2 - b^2 = (a+b)(a-b)
    # If n is of the form above then return True else return False

    while n % 4 == 0:
        n //= 4
    if n % 8 == 0:
        return True
    return False