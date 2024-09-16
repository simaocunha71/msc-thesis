def max_sub_array_sum(lst, k):
    """
    :param lst: list of integers
    :param k: integer, max sum
    :return: integer, sum of largest contiguous sublist
    """
    max_sum = -1
    current_sum = 0
    for i in range(len(lst)):
        current_sum += lst[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum > k:
            current_sum = 0
    return max_sum



