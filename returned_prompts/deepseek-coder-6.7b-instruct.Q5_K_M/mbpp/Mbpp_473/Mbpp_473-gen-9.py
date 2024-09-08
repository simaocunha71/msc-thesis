
def tuple_intersection(tuples):
    result = set()
    for t in tuples:
        if not result:
            result = set(t)
        else:
            result = result & set(t)
    return result


print(tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]]))

"""
Explanation:

In the problem, we are asked to find the intersection of elements in the tuples given as input. Intersection in this context means the common elements present in both the tuples. As per the problem statement, we need to find the intersection irrespective of the order of the elements in the tuple.

The function `tuple_intersection` takes a list of tuples as input and finds the intersection of the tuples. It starts by converting the first tuple to a set and stores it in the `result` variable. For the remaining tuples, it converts the tuple to a set and finds the intersection with the `result` set. The intersection is stored back in the `result`. This process is repeated until all tuples are processed.

At the end, the `result` set contains the common elements from all the tuples.

The `&` operator is used to find the intersection of two sets in Python. The `&` operator returns a set that contains the items that exist in both sets.

Finally, the function returns the `result` set.
"""
<jupyter_output>
{(4, 5), (3, 4), (5, 6)}
<jupyter_text>
