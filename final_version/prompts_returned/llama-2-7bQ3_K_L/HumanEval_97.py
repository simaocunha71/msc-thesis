
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    
    product = 0
    if a > 0 and b > 0:
        while a >= 1:
            product += (b % 10) * ((a % 10) ** 2)
            a, b = a // 10, b - (b / 10)
    elif not (a > 0 and b < 0):
        return 0
    
    return product