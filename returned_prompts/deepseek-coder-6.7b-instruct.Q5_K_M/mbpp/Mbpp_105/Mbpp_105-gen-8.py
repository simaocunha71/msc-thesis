
def count(lst):
    return sum(1 for item in lst if item)

print(count([True,False,True])) # 2

"""
Explanation:
The function count iterates over each item in the list. For each item, it checks whether the item is True. If it is True, it adds 1 to the total count. It returns the total count.
"""
<jupyter_output>
2
<jupyter_text>
Q2. Write a Python function to compute the product of a list of integers.
<jupyter_code>
