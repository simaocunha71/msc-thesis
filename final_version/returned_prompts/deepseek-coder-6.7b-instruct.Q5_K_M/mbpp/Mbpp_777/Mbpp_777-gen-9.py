def find_sum(lst):
    return sum(set(lst))

assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""
Explanation:
The function works by converting the list to a set, which automatically removes any duplicate elements. Then it sums up all the elements in the set.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
