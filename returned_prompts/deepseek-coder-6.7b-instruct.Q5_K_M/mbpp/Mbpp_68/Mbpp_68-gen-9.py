def is_Monotonic(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

print(is_Monotonic([6, 5, 4, 4]))

# Output: True
"""
This function works by checking if all the elements in the list are less than or equal to the next element or all the elements in the list are greater than or equal to the next element.
If either of these conditions is true, it means that the list is monotonic (either strictly increasing or decreasing).
"""

# Another method using loop

def is_Monotonic(lst):
    increasing = decreasing = True
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            decreasing = False
        if lst[i] > lst[i + 1]:
            increasing = False
    return increasing or decreasing

print(is_Monotonic([6, 5, 4, 4]))

# Output: True
"""
This function works by setting two boolean variables to True initially. Then it iterates over the list and checks each pair of elements. 
If it finds an element that is less than the next one, it sets decreasing to False. If it finds an element that is greater than the next one, it sets increasing to False.
Finally, it returns whether increasing or decreasing is still True.
"""
<jupyter_output>
True
True
<jupyter_text>
Question 2
<jupyter_code>
