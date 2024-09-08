
def Split(l):
    return [i for i in l if i % 2 != 0]

print(Split([1,2,3,4,5,6]))

"""
In this function, we're using a list comprehension to iterate through the input list, l. For each item, we check if it's not divisible by 2 (i.e., it's odd). If it's not divisible by 2 (i.e., the remainder of the division is not zero), we include it in the output list.
"""
<jupyter_output>
[1, 3, 5]
<jupyter_text>
Question 2:
<jupyter_code>
