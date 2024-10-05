
    return sorted(set([i for i in l1 if i in l2]))

print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))

#output:
#[1, 5, 653]
#[2, 3]
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:Write a Python function that will take a list of numbers and return a list of tuples, where each tuple contains a number from the original list and its corresponding index in the original list.
<jupyter_code>
