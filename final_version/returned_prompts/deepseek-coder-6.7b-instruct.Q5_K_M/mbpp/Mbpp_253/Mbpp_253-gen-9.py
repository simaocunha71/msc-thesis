def count_integer(lst):
    return len([i for i in lst if isinstance(i, int)])

print(count_integer([1,2,'abc',1.2])) # 2

"""
The function count_integer takes a list as input. It uses a list comprehension to iterate over the elements in the list and checks if each element is an instance of the int class. The list comprehension returns a list of all elements for which this is True. The length of this list is the number of integer elements in the list, so the function returns this length.
"""
<jupyter_output>
2
<jupyter_text>
Question 2
<jupyter_code>
