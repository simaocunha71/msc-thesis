
def even_position(lst):
    return all(i % 2 == 0 for i in lst[::2])

print(even_position([3,2,1]))
<jupyter_output>
False
<jupyter_text>
Q2.
<jupyter_code>
