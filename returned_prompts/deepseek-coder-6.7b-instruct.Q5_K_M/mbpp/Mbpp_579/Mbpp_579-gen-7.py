def find_dissimilar(t1, t2):
    return tuple(x for x in t1 if x not in t2) + tuple(x for x in t2 if x not in t1)

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))

#output: (3, 6, 7, 10)

"""
In this function, we are using a combination of tuple and generator expressions. 
The first part of the function (x for x in t1 if x not in t2) finds elements in the first tuple (t1) that are not in the second tuple (t2). 
The second part of the function (x for x in t2 if x not in t1) does the same for the second tuple. 
The tuple() function is used to convert the generator expressions into tuples. 
The + operator is used to concatenate these two tuples.
"""
<jupyter_output>
(3, 6, 7, 10)
<jupyter_text>
Question 2
<jupyter_code>
