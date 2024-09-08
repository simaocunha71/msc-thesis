
def unique_sublists(lst):
    result = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in result:
            result[tuple_sublist] += 1
        else:
            result[tuple_sublist] = 1
    return result

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
<jupyter_output>
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
<jupyter_text>
Exercise 3: Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.
<jupyter_code>
