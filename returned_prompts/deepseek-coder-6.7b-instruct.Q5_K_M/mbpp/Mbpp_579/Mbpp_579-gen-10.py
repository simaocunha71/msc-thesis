def find_dissimilar(t1, t2):
    set1, set2 = set(t1), set(t2)
    return tuple(set1 ^ set2)

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))

"""
The function find_dissimilar takes two tuples as arguments. It converts each tuple to a set and finds the symmetric difference between the two sets (elements that are in one set but not in the other). The symmetric difference is returned as a tuple.
"""
<jupyter_output>
(3, 6, 7, 10)
<jupyter_text>
Question 3
<jupyter_code>
