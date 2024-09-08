def neg_nos(lst):
    return [i for i in lst if i < 0]

print(neg_nos([-1,4,5,-6]))

# OR

def neg_nos(lst):
    return list(filter(lambda x: x < 0, lst))

print(neg_nos([-1,4,5,-6]))

# Both will return [-1,-6] as expected.
<jupyter_output>
[-1, -6]
[-1, -6]
<jupyter_text>
**