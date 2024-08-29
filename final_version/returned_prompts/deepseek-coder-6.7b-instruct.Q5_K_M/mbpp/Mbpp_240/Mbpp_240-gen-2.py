def replace_list(list1, list2):
    list1[-1:] = list2
    return list1

print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))

"""
In this function, we use the concept of list slicing to replace the last element of the first list with the elements of the second list. The slice list1[-1:] is used to select the last element of the list and it returns a list with that element. So, when we assign list2 to list1[-1:], it replaces the last element of list1 with the elements of list2.
"""

"""
This is a good example of using Python's built-in functions and features to solve problems in a clean and efficient way. Python's list slicing feature is a powerful tool that can make code more readable and concise.
"""
<jupyter_output>
[1, 3, 5, 7, 9, 2, 4, 6, 8]
<jupyter_text>
Question 4
<jupyter_code>
