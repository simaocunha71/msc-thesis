def max_aggregate(my_list):
    """
    Args:
        my_list (list): list of tuples where each tuple contains a name and a score
    Returns:
        tuple: the tuple with the highest score
    """
    return max(my_list, key=lambda x: x[1])
