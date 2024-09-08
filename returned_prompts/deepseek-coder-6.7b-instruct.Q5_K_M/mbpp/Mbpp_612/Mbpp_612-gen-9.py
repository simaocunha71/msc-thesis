def merge(lst):
    return [[sub[i] for sub in lst] for i in range(2)]

# test
print(merge([['x',  'y'], ['a',  'b'], ['m',  'n']])) # should return [['x', 'a', 'm'], ['y', 'b', 'n']]

"""
Explanation:

The function `merge` takes a list of lists as input. It uses a list comprehension to create two lists:
1) The first list is created by iterating over the sublists and selecting the i-th element for each sublist, where i is 0 (i.e., the first element of each sublist).
2) The second list is created in a similar way, but i is 1 (i.e., the second element of each sublist).

Finally, the function returns a new list containing the two lists created in the previous steps.
"""
<jupyter_output>
[['x', 'a', 'm'], ['y', 'b', 'n']]
<jupyter_text>
Q3. Write a Python program to find unique values in a list.
<jupyter_code>
def unique_values(lst):
    return list(set(lst))

# test
print(unique_values([1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 8, 8])) # should return [1, 2, 3, 4, 5, 6, 7, 8]
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7, 8]
<jupyter_text>
Q4. Write a Python program to find the intersection of two lists.
<jupyter_code>
def intersect(lst1, lst2):
    return list(set(lst1) & set(lst2))

# test
print(intersect([1, 2, 2, 3, 4], [2, 2, 4, 5,