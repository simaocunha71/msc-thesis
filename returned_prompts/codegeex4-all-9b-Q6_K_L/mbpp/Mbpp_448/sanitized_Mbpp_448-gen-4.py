def cal_sum(n):
    """
    Calculate the sum of perrin numbers up to the nth number.

    :param n: int, the nth number to calculate the sum up to.
    :return: int, the sum of perrin numbers up to the nth number.
    """
    perrin = [0, 2, 3]
    if n < 3:
        return sum(perrin[:n+1])
    for i in range(3, n+1):
        perrin.append(perrin[i-2] + perrin[i-3])
    return sum(perrin)