
def largest_smallest_integers(lst):
    # Initialize the variables
    max_neg = None
    min_pos = None

    # Iterate through the list
    for num in lst:
        # If the number is negative and larger than max_neg, update max_neg
        if num < 0 and (max_neg is None or num > max_neg):
            max_neg = num
        # If the number is positive and smaller than min_pos, update min_pos
        if num > 0 and (min_pos is None or num < min_pos):
            min_pos = num

    # If no negative or positive number is found, return None for both
    if max_neg is None and min_pos is None:
        return (None, None)

    # Otherwise, return the found max_neg and min_pos
    return (max_neg, min_pos)

# Testing
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)
print(largest_smallest_integers([-3, 1, 0, 4]))  # (-3, 1)

























































































































































































