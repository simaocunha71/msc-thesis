def pair_wise(lst):
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]
"""
In this function, we are using list comprehension to generate the pairs. We are iterating over the indices of the list, up to the second last element (since we are trying to pair the current element with the next one). For each index, we are creating a pair of current element and the next one and adding it to the resultant list. Finally, we are returning the resultant list.
"""

# Testing the function
print(pair_wise([1, 1, 2, 3, 3, 4, 4, 5]))

"""
In the output, we are getting a list of tuples where each tuple contains two elements from the original list. The tuples are pairs of consecutive elements from the original list.
"""
<jupyter_output>
[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
<jupyter_text>
Question 2:
<jupyter_code>
