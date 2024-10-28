
def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda tup: (tup[0], -tup[1]))
    return coordinates

print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1)) # [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1)) # []
print(get_row([[], [1], [1, 2, 3]], 3)) # [(2, 2)]

This function works by iterating over each row and column in the list. If the element at the given coordinate is equal to x, it adds the coordinate to a list of tuples. This list of tuples is then sorted first by rows in ascending order, and then by columns in descending order. The lambda function is used to specify the sorting order.

The time complexity of this function is O(n*m) where n is the number of rows and m is the number of columns in the list.

The space complexity is also O(n*m) because in the worst case, each element in the list could be equal to x and so a tuple would be added to the list for each element.
"""

# Test cases:
print(get_row([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
], 1))

print(get_row([], 1))

print(get_row([[], [1], [1, 2, 3]], 3))
<jupyter_output>
[(0, 0), (1, 4), (1, 0), (