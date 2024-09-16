def is_Monotonic(my_list):
    """
    :param my_list: array to be checked
    :return: True if array is monotonic, False otherwise
    """
    if len(my_list) <= 1:
        return True
    return all(my_list[i] <= my_list[i + 1] for i in range(len(my_list) - 1))
