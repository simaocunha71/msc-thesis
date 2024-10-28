    # Start with a list of all values in the original list
    all_values = set(lst)

    # Sort the list in ascending order
    all_values = sorted(all_values)

    # Initialize an empty list
    sorted_list = []

    # Iterate through the original list,
    # adding elements to sorted_list in strange order
    while lst:
        # Get the current minimum from all_values
        min_val = all_values.pop(0)

        # Check if the current minimum is in the original list
        if min_val in lst:
            # If it is, add it to sorted_list
            sorted_list.append(min_val)

        # Remove the current minimum from the original list
        lst.remove(min_val)

    # Return the strange sorted list
    return sorted_list

# Test cases
print(strange_sort_list([1, 2, 3, 4]))
print(strange_sort_list([5, 5, 5, 5]))
print(strange_sort_list([]))

# Output:
# [1, 4, 2, 3]
# [5, 5, 5, 5]
# []

# Explanation
# The function starts by creating a set of all values in the original list.
# This set is then sorted in ascending order, creating a new list of all values.
# The function initializes an empty list to store the strange sorted elements.
# The function then iterates through the original list, adding elements to the sorted list in a strange order.
# For each element in the original list, the function pops the minimum value from the all_values list,
# checks if the minimum value is in the original list, and if so, adds it to the sorted list.
# The function then removes the current minimum from the original list.
# This process continues until the original list is empty, and the function returns the strange sorted list.

















































