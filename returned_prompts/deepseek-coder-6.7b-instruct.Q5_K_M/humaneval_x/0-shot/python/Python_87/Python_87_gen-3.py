
def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coordinates.append((i, j))
    return sorted(coordinates, key=lambda x: (x[0], -x[1]))

# Test cases
print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1))  # [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1))  # []
print(get_row([[], [1], [1, 2, 3]], 3))  # [(2, 2)]

In this code, we iterate over each sublist (row) and its elements (columns), and check if the element is equal to x. If it is, we append the tuple (row index, column index) to the coordinates list. We sort the coordinates first by row index in ascending order, and then by column index in descending order. We return this sorted list of tuples.
<jupyter_output>
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
[]
[(2, 2)]
<jupyter_text>
**Task 2**Given a string of words separated by spaces, write a function that returns the length of the last word in the string.
<jupyter_code>
