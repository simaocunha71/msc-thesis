
def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result

# Test cases
print(get_row([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1))  # [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1))  # []
print(get_row([[], [1], [1, 2, 3]], 3))  # [(2, 2)]

# Sort the list of tuples by row in ascending order and then by column in descending order.
# The lambda function is used to specify that the sorting should be first by the first element of each tuple (i.e., the row)
# and then by the second element of each tuple (i.e., the column), with the column being sorted in descending order.
# This is accomplished by using the minus sign (-) before the second element of the tuple.
<jupyter_output>
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
[]
[(2, 2)]
<jupyter_text>
