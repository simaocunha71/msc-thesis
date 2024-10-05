    array_copy = array.copy()  # Create a copy of the array
    if sum(array_copy[0], array_copy[-1]) % 2 == 0:
        array_copy.sort(reverse=True)  # Sort in descending order
    else:
        array_copy.sort()  # Sort in ascending order
    return array_copy


