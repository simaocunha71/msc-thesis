
def odd_position(lst):
    return all(x % 2 == 1 for x in lst[::2])

print(odd_position([2,1,4,3,6,7,6,3]))
<jupyter_output>
True
<jupyter_text>
Question 2
<jupyter_code>
