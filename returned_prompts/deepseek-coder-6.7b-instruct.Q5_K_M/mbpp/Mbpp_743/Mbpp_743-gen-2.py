def rotate_right(lst, k):
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

"""
Explanation:
Here, we are given a list and a number k. We rotate the list to the right by k items. This is done by slicing the list at the point k from the end and combining the two slices in the order they were obtained. The [-k:] slice gives the last k elements of the list and the [:-k] slice gives the rest of the elements in the list.

When we execute the code with the given example, it will return [8, 9, 10, 1, 2, 3, 4, 5, 6, 7] which is the expected result.
"""
<jupyter_output>
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
<jupyter_text>
Question 2
<jupyter_code>
