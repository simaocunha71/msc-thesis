
def add_tuple(lst, tup):
    return lst + list(tup)

print(add_tuple([5, 6, 7], (9, 10)))

# Output: [5, 6, 7, 9, 10]

# The function add_tuple takes two arguments: a list and a tuple. It converts the tuple to a list using list() and then adds this list to the original list using the + operator. The result is the original list extended by the elements of the tuple.
<jupyter_output>
[5, 6, 7, 9, 10]
<jupyter_text>
Question 2:
<jupyter_code>
