
def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    result.sort(key=lambda y: (y[0], -y[1]))
    return result

print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1))
print(get_row([], 1))
print(get_row([[], [1], [1, 2, 3]], 3))


"""
In this code, we first initialize an empty list result to store the tuples of coordinates.
We then loop over each sublist in lst with its index i. For each sublist, we loop over each element with its index j. If the element is equal to x, we append a tuple of the form (i, j) to result.
Finally, we sort result by the first element of each tuple in ascending order, and by the second element of each tuple in descending order. We return the sorted result.
"""

# Code by: Sruti Bhargav
<jupyter_output>
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
[]
[(2, 2)]
<jupyter_text>
Question 2:
<jupyter_code>
