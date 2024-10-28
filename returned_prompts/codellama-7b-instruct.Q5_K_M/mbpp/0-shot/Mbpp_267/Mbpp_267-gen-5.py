def square_Sum(n):
    """
    :param n: integer
    :return: sum of the squares of the first n odd natural numbers
    """
    sum = 0
    for i in range(1, n + 1, 2):
        sum += i ** 2
    return sum


