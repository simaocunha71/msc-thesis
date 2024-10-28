    # Initialize result list
    result = []

    # Loop until all numbers are processed
    while len(lst) > 0:
        # Find the minimum value in the list
        min_value = min(lst)

        # Append the minimum value to the result list
        result.append(min_value)

        # Filter the list to exclude the minimum value
        lst = [num for num in lst if num != min_value]

        # If there are no remaining numbers, break the loop
        if len(lst) == 0:
            break

        # Find the maximum value in the remaining list
        max_value = max(lst)

        # Append the maximum value to the result list
        result.append(max_value)

        # Filter the list to exclude the maximum value
        lst = [num for num in lst if num != max_value]

    # Return the result list
    return result


# Test the function
print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
print(strange_sort_list([]))  # Output: []


































































































































































































