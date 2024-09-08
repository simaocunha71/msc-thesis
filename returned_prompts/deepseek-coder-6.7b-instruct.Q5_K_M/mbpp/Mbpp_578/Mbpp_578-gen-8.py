
def interleave_lists(a, b, c):
    return [val for pair in zip(a, b, c) for val in pair]

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))
"""
This function uses the built-in zip function to create tuples of corresponding elements from each input list. It then uses a list comprehension to flatten these tuples into a single list.
"""
<jupyter_output>
[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
<jupyter_text>
Q12.
<jupyter_code>
