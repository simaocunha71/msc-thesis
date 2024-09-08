def split_two_parts(lst, L):
    return (lst[:L], lst[L:])

print(split_two_parts([1,1,2,3,4,4,5,1],3))

# Output: ([1, 1, 2], [3, 4, 4, 5, 1])

# Explaination:
# The function split_two_parts takes a list and an integer L as input.
# It returns a tuple where the first element is the first L elements of the list, and the second element is the remaining elements of the list after the first L elements have been removed.
<jupyter_output>
([1, 1, 2], [3, 4, 4, 5, 1])
<jupyter_text>
Question 3:
<jupyter_code>
