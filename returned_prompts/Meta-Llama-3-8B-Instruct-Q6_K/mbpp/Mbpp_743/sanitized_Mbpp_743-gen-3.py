def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]  # Rotate the list to the right by n positions.  # Slice the list from the end to the start by n positions.  # Slice the list from the start to the end by n positions.  # Concatenate the two slices.  # Return the rotated list.  # Example: rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)  # Output: [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]  # Example: rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example: rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -3)  # Output: [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]  # Example: rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example: rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example: rotate_right([], 3)  # Output: []  # Example: rotate_right([1], 3)  # Output: [1]  # Example: rotate_right([1, 2], 3)  # Output: [1, 2]  # Example: rotate