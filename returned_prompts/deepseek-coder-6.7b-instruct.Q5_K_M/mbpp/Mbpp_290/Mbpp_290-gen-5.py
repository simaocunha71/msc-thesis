def max_length(lst):
    max_len = len(max(lst, key=len))
    max_lst = [lst[i] for i in range(len(lst)) if len(lst[i]) == max_len]
    return max_len, max_lst

# test
print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# Output: (3, [[13, 15, 17]])
"""
Explanation:
The function max_length takes a list of lists as input. 
It uses the built-in Python function max with the key parameter set to len to find the list with the maximum length. 
Then it collects all the lists with the maximum length into a new list. 
Finally, it returns the maximum length and the new list.
"""

"""
The time complexity of this function is O(n), where n is the number of elements in the input list. This is because it scans the list of lists once to find the maximum length, and then scans the list of lists again to collect all the lists with that maximum length.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
