
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, cell in enumerate(row):
            if cell == x:
                result.append((i, j))
    return sorted(result, key=lambda tup: (tup[0], -tup[1]))


print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1))
print(get_row([], 1))
print(get_row([[], [1], [1, 2, 3]], 3))

# Returns:
# [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
# []
# [(2, 2)]


# The function works by iterating over the rows and columns of the given list,
# checking if the cell's value matches the target number.
# If it does, it adds the row and column indices to a list.
# Finally, it sorts the list by rows in ascending order and columns in descending order before returning it.

# This solution has a time complexity of O(n*m), where n is the number of rows in the list and m is the average number of columns in the rows.
# The space complexity is also O(n*m), in the worst case when all cells match the target number.

# This is because we have to go through every cell in the list to check if it matches the target number.
# If it does, we store the corresponding indices in a new list.
# We then sort this list, which takes O(n*m*log(n*m)) time.
# The space complexity is O(n*m) because in the worst case (when every cell matches the target number), we store all of the indices in the list.
<jupyter_output>
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
[]
[(2, 2)]
<j