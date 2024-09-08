def union_elements(t1, t2):
    return tuple(sorted(set(t1 + t2)))

print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))

"""
Explanation:
The function union_elements takes two tuples t1 and t2 as input. The + operator is used to concatenate the two tuples, and set() is used to convert the result to a set which automatically removes duplicate elements. The sorted() function is used to sort the resulting elements in ascending order. Finally, the function returns the result as a tuple.
"""
<jupyter_output>
(3, 4, 5, 6, 7, 10)
<jupyter_text>
Question 2:
<jupyter_code>
