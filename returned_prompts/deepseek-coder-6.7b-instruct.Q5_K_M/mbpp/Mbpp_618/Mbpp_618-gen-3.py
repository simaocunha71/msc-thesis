def div_list(list1, list2):
    return [a / b for a, b in zip(list1, list2)]

print(div_list([4,5,6],[1, 2, 3]))

# Expected output:
# [4.0, 2.5, 2.0]

# Explanation:
# The function div_list takes two lists as arguments.
# It uses the zip function to pair up the elements from the two lists together.
# Then it uses a list comprehension to divide each pair of elements from the lists.
# The result is a new list that contains the division results.
# The function returns this new list.

# Note:
# This function assumes that the two lists are of the same length and that the second list does not contain zero.
# If these assumptions are not true, the function will raise an error.
<jupyter_output>
[4.0, 2.5, 2.0]
<jupyter_text>
Problem 2
<jupyter_code>
