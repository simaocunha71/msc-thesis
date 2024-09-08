def sum_list(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

print(sum_list([10,20,30],[15,25,35]))

"""
Another way to solve this problem is to use the map function.
"""

def sum_list(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

print(sum_list([10,20,30],[15,25,35]))

"""
Both codes do the same thing but the first one uses a list comprehension while the second one uses the map function.
"""
<jupyter_output>
[25, 45, 65]
[25, 45, 65]
<jupyter_text>
Question 2:
<jupyter_code>
