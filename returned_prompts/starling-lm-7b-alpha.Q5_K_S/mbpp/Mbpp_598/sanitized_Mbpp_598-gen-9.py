def armstrong_number(num):
    """
    Args:
        num (int): The number to check
    Returns:
        bool: True if the number is an armstrong number, False otherwise
    """
    n = len(str(num))
    sum_of_cubes = 0
    temp = num
    while temp>0:
        sum_of_cubes += (temp%10)**n
        temp //= 10
    return sum_of_cubes == num