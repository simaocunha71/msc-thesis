
def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                coordinates.append((i, j))
    coordinates.sort(key=lambda x: (x[0], -x[1]))
    return coordinates
<jupyter_output>
<empty_output>
<jupyter_text>
Test Cases
<jupyter_code>
print(get_row([[1,2,3,4,5,6],[1,2,3,4,1,6],[1,2,3,4,5,1]], 1)) #  [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
print(get_row([], 1)) #  []
print(get_row([[], [1], [1, 2, 3]], 3)) # [(2, 2)]
<jupyter_output>
[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
[]
[(2, 2)]
<jupyter_text>
The above solution works by iterating over each sublist in the given list and checking if the element at index `j` is equal to `x`. If so, the coordinates `(i, j)` are appended to a list. The list is then sorted first by rows in ascending order, and then by columns in descending order. The `lambda` function is used as a key to sort the coordinates by rows first and columns second. The `-x[1]` is used to sort the columns in descending order.
<jupyter_code>

<jupyter_output>
<empty_output>
<jupyter_text>
Question 1
<jupyter_code>
def question1():
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0