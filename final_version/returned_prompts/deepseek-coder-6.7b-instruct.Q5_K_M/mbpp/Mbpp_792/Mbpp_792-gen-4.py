
def count_list(l):
    return len(l)

print(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# or

def count_list(l):
    count = 0
    for i in l:
        if isinstance(i, list):
            count += 1
    return count

print(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# or

def count_list(l):
    count = 0
    for i in l:
        if type(i) is list:
            count += 1
    return count

print(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))

"""
All these functions work the same way: they go through each element in the given list and check if it's an instance of list (using isinstance) or if it's a list itself (using type). If it is, they increase the counter. In the end, the counter gives the number of lists in the list.
"""
<jupyter_output>
4
4
4
<jupyter_text>
Problem 2
<jupyter_code>
