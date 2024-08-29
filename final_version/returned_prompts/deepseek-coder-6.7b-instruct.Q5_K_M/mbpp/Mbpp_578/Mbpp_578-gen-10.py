def interleave_lists(lst1, lst2, lst3):
    result = []
    for i in range(len(lst1)):
        result.extend([lst1[i], lst2[i], lst3[i]])
    return result

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))

"""
Explanation:
The function interleave_lists takes three lists as arguments. It initializes an empty list result.
It then iterates over the range of the length of the first list. For each index, it adds the element of the first list at that index, the second list at that index, and the third list at that index to result. This is done using the extend method, which adds all items of a list to another list.
Finally, it returns the result.
"""

# Alternative solution using zip function:

def interleave_lists(lst1, lst2, lst3):
    return [item for sublist in zip(lst1, lst2, lst3) for item in sublist]

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))

"""
Explanation:
This alternative solution uses the built-in Python function zip, which makes an iterator that aggregates elements from each of the iterables. The zip function is used here to interleave the three input lists. The result is a list of tuples where each tuple contains the corresponding elements from the input lists. The list comprehension then flattens this into a single list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
