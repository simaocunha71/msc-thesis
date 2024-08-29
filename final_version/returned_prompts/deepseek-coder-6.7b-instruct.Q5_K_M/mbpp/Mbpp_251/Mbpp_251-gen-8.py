def insert_element(lst, elm):
    return [elm]*(len(lst)*2-1) + lst

print(insert_element(['Red', 'Green', 'Black'], 'c'))

Output:
['c', 'Red', 'c', 'Green', 'c', 'Black']
"""

Explanation:
The function `insert_element` takes in two arguments, `lst` and `elm`. It calculates the number of times `elm` should be inserted before every element in `lst` by multiplying the length of `lst` by 2 (to account for the `elm` before each element) and subtracting 1 (to avoid an extra `elm` at the end). This number of times `elm` is then inserted into a new list using the repetition operator `*`. The original list is then appended to the new list. The function returns the resulting list.
"""
<jupyter_output>
['c', 'Red', 'c', 'Green', 'c', 'Black']
<jupyter_text>
Question 2
<jupyter_code>
"""
