def Extract(lst):
    return [i[0] for i in lst]

print(Extract([[1, 2], [3, 4, 5], [6, 7, 8, 9]]))

# Output: [1, 3, 6]

# Explanation:
# This function works by using list comprehension to iterate over each sublist in the main list. The expression "i[0]" in the list comprehension is used to get the first element of each sublist, which is the first element of the list that corresponds to the current iteration.
# The result is a new list that contains the first elements of all the sublists.
<jupyter_output>
[1, 3, 6]
<jupyter_text>
Question 3
<jupyter_code>
