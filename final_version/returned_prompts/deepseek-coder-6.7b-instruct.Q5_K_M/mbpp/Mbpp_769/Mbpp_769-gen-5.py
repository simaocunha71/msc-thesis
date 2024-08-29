def Diff(li1, li2):
    return list(set(li1) - set(li2))

li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]

print(Diff(li1, li2))

"""
In the above python program, we have defined a function Diff which takes two lists as inputs. Inside the function, we have used the set() function which returns a set of distinct elements from the list. We then subtracted the second list from the first list and returned the result as a list using list() function.
"""

"""
In this program, we have used the set data type in Python, which is an unordered collection of unique elements. We then subtract the set of li2 from the set of li1 and return the result as a list. The set data type in Python provides an efficient way to handle unique elements.
"""

"""
The output of this program will be:
[10, 20, 30, 15]
"""

"""
This output means that the elements [10, 20, 30, 15] are present in the first list but not in the second list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
