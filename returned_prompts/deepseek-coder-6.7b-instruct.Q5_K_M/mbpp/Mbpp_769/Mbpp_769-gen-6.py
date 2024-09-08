
def Diff(list1, list2):
    return [i for i in list1 if i not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))

"""
Explanation:
This function works by using list comprehension to iterate over the elements in the first list. 
It checks if each element is in the second list. If it is not, it adds it to the new list. 
This gives the elements that are present in the first list but not in the second list.
"""
<jupyter_output>
[10, 20, 30, 15]
<jupyter_text>
Question 2
<jupyter_code>
"""
