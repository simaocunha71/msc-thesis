    # This function returns True if the list is sorted in ascending order.
    # If the list has more than 1 duplicate of the same number, then it returns False.
    # Assume that the list only has positive integers and no negative numbers.

    # Initialize the counter for the number of duplicate values to 0
    duplicate_count = 0

    # Iterate through the list using a for loop
    for i in range(len(lst)-1):
        # If the current element is greater than the next element, then it is not sorted in ascending order
        if lst[i] > lst[i+1]:
            # If the list is not sorted in ascending order, then it returns False
            return False
        # If the current element is equal to the next element, then increment the duplicate counter
        elif lst[i] == lst[i+1]:
            duplicate_count += 1
            # If the duplicate counter is greater than 1, then it returns False
            if duplicate_count > 1:
                return False

    # If the function has not returned False yet, then the list is sorted in ascending order and it returns True
    return True

# Call the function with the given test cases
print(is_sorted([5]))  # True
print(is_sorted([1, 2, 3, 4, 5]))  # True
print(is_sorted([1, 3, 2, 4, 5]))  # False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # False

# End of program







# Here is a Python program that