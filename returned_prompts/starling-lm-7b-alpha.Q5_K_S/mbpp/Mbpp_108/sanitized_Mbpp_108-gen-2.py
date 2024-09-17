from itertools import chain
def merge_sorted_list(list1, list2, list3):
    """
    Merge three lists into a single sorted list.
    """
    # Merge the first two lists
    merged_list = sorted(list1 + list2)
    # Merge the merged list with the third list
    merged_list = sorted(merged_list + list3)
    return merged_list