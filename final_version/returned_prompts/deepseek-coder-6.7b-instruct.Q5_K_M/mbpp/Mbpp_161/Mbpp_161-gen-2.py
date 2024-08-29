def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))

"""
Explanation:
This function uses list comprehension to iterate over each element in the first list (lst1). If the element is not in the second list (lst2), it is included in the new list.
"""
<jupyter_output>
[1, 3, 5, 7, 9, 10]
<jupyter_text>
5. Write a function to find the second largest number in a list.
<jupyter_code>
