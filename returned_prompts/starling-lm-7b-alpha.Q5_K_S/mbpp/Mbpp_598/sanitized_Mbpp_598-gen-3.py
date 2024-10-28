def armstrong_number(num):
    """
    Args:
        num: The number to check

    Returns:
        True if the number is armstrong, False otherwise
    """
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for i in range(num_len):
        sum += (int(num_str[i]) ** num_len)
    if sum == num:
        return True
    return False