def union_elements(t1, t2):
    union = t1 + t2
    return tuple(sorted(union))

print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))


"""
Explanation:

The function `union_elements` takes two tuples as arguments. It concatenates the two tuples using the `+` operator and returns the result. It then sorts the elements of the resulting tuple using the `sorted` function and returns the result.
"""
<jupyter_output>
(3, 4, 5, 6, 7, 10)
<jupyter_text>
Exercise 5: Write a function to find the intersection of the elements of two given tuples.
<jupyter_code>
