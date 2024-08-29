def replace_list(list1, list2):
    list1[-1] = list2
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

"""
Replace_list function takes two lists as arguments. It replaces the last element of the first list with the elements of the second list using list1[-1] = list2. Finally, it returns the modified first list.
"""
<jupyter_output>
[1, 3, 5, 7, 9, [2, 4, 6, 8]]
<jupyter_text>
**2. Write a Python program to find the second largest number in a list.**
<jupyter_code>
