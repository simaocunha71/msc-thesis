
def remove_elements(list1, list2):
    list3 = [i for i in list1 if i not in list2]
    return list3

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

"""
In this code, we use list comprehension to iterate through list1 and include only those elements that are not present in list2.
"""
<jupyter_output>
[1, 3, 5, 7, 9, 10]
<jupyter_text>
3. Write a Python function to find the second largest number in a list.
<jupyter_code>
