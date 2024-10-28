
def get_row(lst, x):
    coords = []
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                coords.append((i, j))
    return sorted(coords, key=lambda tup: (tup[0], -tup[1]))

print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1))
print(get_row([], 1))
print(get_row([[], [1], [1, 2, 3]], 3))

# Output:
# [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
# []
# [(2, 2)]
<jupyter_output>
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
[]
[(2, 2)]
<jupyter_text>
Question 2
<jupyter_code>
