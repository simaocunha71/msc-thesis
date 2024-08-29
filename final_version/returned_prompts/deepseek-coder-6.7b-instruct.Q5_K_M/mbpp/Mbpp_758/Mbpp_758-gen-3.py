
def unique_sublists(lst):
    dic = {}
    for sublist in lst:
        tup = tuple(sublist)
        if tup in dic:
            dic[tup] += 1
        else:
            dic[tup] = 1
    return dic

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

"""
The function works by iterating through each sublist in the provided list. It converts each sublist to a tuple and checks if this tuple is in the dictionary. If it is, it increments the corresponding value by 1. If it's not, it adds the tuple to the dictionary with a value of 1.
"""
<jupyter_output>
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
<jupyter_text>
Problem 4: List of tuples to dictionary
<jupyter_code>
