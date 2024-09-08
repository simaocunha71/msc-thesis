def find_sum(lst):
    return sum(set(lst))

print(find_sum([1,2,3,1,1,4,5,6])) # 21

"""
In this solution, we are first converting the list to a set. A set in python is a collection which is unordered and unindexed. It also doesn't allow duplicate values. So by converting the list to a set, we remove all the duplicates.
Then we use the built-in sum function to find the sum of all elements in the set.
"""
<jupyter_output>
21
<jupyter_text>
Problem 4
<jupyter_code>
