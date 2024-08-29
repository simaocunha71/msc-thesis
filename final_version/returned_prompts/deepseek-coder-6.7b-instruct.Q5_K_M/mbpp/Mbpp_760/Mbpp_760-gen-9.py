def unique_Element(lst):
    return len(set(lst)) == 1

print(unique_Element([1,1,1])) # True
print(unique_Element([1,2,3])) # False


"""
Explanation:

The function unique_Element takes a list lst as input.
The set function is used to convert the list into a set, which removes any duplicated elements.
Then, the length of the set is compared with the length of the list. If the lengths are the same, it means that all elements in the list are the same.
If the lengths are not the same, it means that there are at least two distinct elements in the list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
