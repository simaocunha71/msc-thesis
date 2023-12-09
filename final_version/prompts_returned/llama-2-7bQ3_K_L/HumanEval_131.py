
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    sum = 0
    for i in range(1, n // 2 + 1):
        if n % 2 != 0: # odd
            sum += int((n//i)*i)
    
    return sum

def main():
    print digits(54372)