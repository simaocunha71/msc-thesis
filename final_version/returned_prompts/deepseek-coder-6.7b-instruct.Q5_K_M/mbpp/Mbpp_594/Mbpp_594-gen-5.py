def diff_even_odd(lst):
    even_num = [i for i in lst if i % 2 == 0]
    odd_num = [i for i in lst if i % 2 != 0]
    return even_num[0] - odd_num[0]

assert diff_even_odd([1,3,5,7,4,1,6,8])==3
"""
The function diff_even_odd takes a list as input, finds the first even and odd numbers in the list, and returns the difference between the first even and odd number.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2
<jupyter_code>
