def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))

"""
The '^' operator is used to find the symmetric difference of two sets. 
The symmetric difference of A and B is a set of elements which are in either of the sets A or B but not in their intersection. 
In other words, it's a set of elements which are in one of the sets but not in both.
"""

# Alternatively, if you want to use list comprehension, you can do:
def find_dissimilar(t1, t2):
    return tuple(x for x in t1 + t2 if (x not in t1) or (x not in t2))

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))

"""
The above function works by first combining the two tuples, then for each element, it checks if it is in either of the tuples. If it is not in either, it adds it to the result.
"""
<jupyter_output>
(3, 6, 7, 10)
(3, 6, 7, 10)
<jupyter_text>
Question 2: Write a function that takes a list of dictionaries as an argument and returns a new list of dictionaries with the same keys but with all the values reversed.
<jupyter_code>
