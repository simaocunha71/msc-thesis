def cal_sum(n):
    """
    Args:
        n: The max number of Perrin number to be calculated.

    Returns:
        The sum of all Perrin number from 1 to n.
    """
    result = 0
    p_list = [1]
    for i in range(n):
        p_list.append(2 * p_list[i] + 1)
        p_list.append(p_list[i] + 1)
        result += sum(p_list[-2::-1])
    return result