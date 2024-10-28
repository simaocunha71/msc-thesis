def merge_sorted_list(list_1, list_2, list_3):
    """
    Merge three lists into a single sorted list.

    Parameters:
    list_1 (list): The first list of numbers.
    list_2 (list): The second list of numbers.
    list_3 (list): The third list of numbers.

    Returns:
    list: The merged list of numbers in sorted order.
    """
    # Merge the three lists into a single list.
    merged_list = list_1 + list_2 + list_3

    # Sort the merged list.
    sorted_list = sorted(merged_list)

    # Return the sorted list.
    return sorted_list