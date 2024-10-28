
    # Create an empty list to hold the coordinates
    coordinates = []

    # Iterate over the rows
    for i in range(len(lst)):
        # Iterate over the columns
        for j in range(len(lst[i])):
            # If the current value is equal to x, append the coordinate to the list
            if lst[i][j] == x:
                coordinates.append((i, j))

    # Sort the coordinates by rows in ascending order, then by columns in descending order
    coordinates.sort(key=lambda x: (x[0], -x[1]))

    return coordinates


# Test cases
print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1)) # Expected: [(0, 0), (0, 5), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1)) # Expected: []
print(get_row([[], [1], [1, 2, 3]], 3)) # Expected: [(2, 2)]
print(get_row([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 1)) # Expected: [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)]

# This solution has a time complexity of O(n) because it traverses all elements in the list once.
# The space complexity is also O(n) because in the worst case scenario, all elements in the list are equal to x,
# so we are storing all the coordinates in the list.

# The function works by iterating over each element in the list and checking if it is equal to x.
# If it is, it adds the coordinate to the list of coordinates. Finally, it sorts the list of coordinates by rows in ascending order,
# and then by columns in descending order before returning it