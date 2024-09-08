
def max_length(lst):
    max_len = max(len(lst[i]) for i in range(len(lst)))
    for i in lst:
        if len(i) == max_len:
            return max_len, i

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

#Answer:
# The function `max_length` finds the maximum length in a list of lists. It first calculates the maximum length of the list of lists using the built-in `max` function and a generator expression. Then it goes through each list in the list of lists, and if the length of the current list is equal to the maximum length, it returns the maximum length and the list itself.
<jupyter_output>
(3, [13, 15, 17])
<jupyter_text>
Problem 3:
<jupyter_code>
