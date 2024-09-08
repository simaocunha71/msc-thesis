def remove_nested(tup):
    new_tup = []
    for i in tup:
        if type(i) != tuple:
            new_tup.append(i)
    return tuple(new_tup)

print(remove_nested((1, 5, 7, (4, 6), 10)))

# Alternatively, you can solve this problem using list comprehension as well:

def remove_nested(tup):
    return tuple(i for i in tup if type(i) != tuple)

print(remove_nested((1, 5, 7, (4, 6), 10)))

# The output of both solutions will be: (1, 5, 7, 10)
<jupyter_output>
(1, 5, 7, 10)
(1, 5, 7, 10)
<jupyter_text>
Problem 7:
<jupyter_code>
