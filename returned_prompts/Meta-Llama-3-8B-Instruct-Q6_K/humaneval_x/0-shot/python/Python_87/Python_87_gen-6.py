    # create a new list to store the coordinates
    coordinates = []
    
    # iterate over the list of lists with enumerate to get the row index
    for i, row in enumerate(lst):
        # find the index of x in the row
        try:
            x_index = row.index(x)
        except ValueError:
            continue
        
        # add the coordinates to the list
        coordinates.append((i, len(row) - 1 - x_index))
    
    # sort the coordinates by row index and column index (in descending order)
    coordinates.sort()
    
    return coordinates
# Test cases
print(get_row([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1)) 
# Expected output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1)) 
# Expected output: []
print(get_row([[], [1], [1, 2, 3]], 3)) 
# Expected output: [(2, 2)]


# Code
def get_row(lst, x):
    coordinates = []
    for i, row in enumerate(lst):
        try:
            x_index = row.index(x)
        except ValueError:
            continue
        coordinates.append((i, len(row) - 1 - x_index))
    coordinates.sort(key=lambda x: (x[0], -x[1]))
    return coordinates
# Test cases
print(get_row([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1)) 
# Expected output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1)) 
# Expected output: []
print(get_row([[], [1], [1, 2, 3]], 3)) 
# Expected output: [(2, 2)]


# Explanation
The function `get_row` takes a list of lists (`lst`) and an integer (`x`) as input. It iterates over the list of lists, and for each row, it finds the index of `x` using the `index` method.