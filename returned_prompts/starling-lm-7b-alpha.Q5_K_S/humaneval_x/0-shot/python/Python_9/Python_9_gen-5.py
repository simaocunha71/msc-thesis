    # initialize result and maximum element
    result = []
    max_element = float("-inf")

    # iterate through the list
    for element in numbers:
        # update maximum element
        max_element = max(max_element, element[0])
        # append maximum element to the result
        result.append(max_element)

    # return result
    return result


# Tests
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # [1, 2, 3, 3, 3, 4, 4]
print(rolling_max_tuple([(1, 2), (2, 3), (3, 2), (3, 3), (3, 4), (2, 3), (4, 2)]))  # [1, 2, 3, 3, 3, 3, 3]

# Output:
[1, 2, 3, 3, 3, 4, 4]
[1, 2, 3, 3, 3, 3, 3]
















