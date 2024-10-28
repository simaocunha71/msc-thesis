def get_median(list1, list2, n):
    # Create a list with both lists
    combined_list = list1 + list2
    # Sort the combined list
    combined_list.sort()
    # Calculate the index of the median element
    median_index = n // 2
    # Check if the median is in the first half or the second half of the combined list
    if median_index < len(combined_list) // 2:
        median = combined_list[median_index]
    else:
        median = combined_list[-median_index-1]
    # Return the median
    return median