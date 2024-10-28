def get_row(lst, x):
    # If the input list is empty, return an empty list
    if not lst:
        return []
    
    # Create an empty list to store the coordinates
    coordinates = []
    
    # Iterate over the rows of the list
    for i, row in enumerate(lst):
        # Iterate over the elements of the row
        for j, element in enumerate(row):
            # If the element is equal to x, add the coordinate to the list
            if element == x:
                coordinates.append((i, j))
    
    # Sort the coordinates first by rows in ascending order
    coordinates.sort(key=lambda coord: coord[0])
    
    # Sort the coordinates of the row by columns in descending order
    coordinates.sort(key=lambda coord: coord[0])
    
    # Return the list of coordinates
    return coordinates

# Test the function with the provided examples
print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1))
print(get_row([], 1))
print(get_row([[], [1], [1, 2, 3]], 3))