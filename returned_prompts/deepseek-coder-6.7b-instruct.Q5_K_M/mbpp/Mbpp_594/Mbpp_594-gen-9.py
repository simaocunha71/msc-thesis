def diff_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even[0] - odd[0] if even and odd else None

print(diff_even_odd([1,3,5,7,4,1,6,8])) # 3

"""
In this function, we first create two lists, one for even numbers and one for odd numbers. We then return the difference of the first number of these two lists if they exist. If not, we return None.
"""
<jupyter_output>
3
<jupyter_text>
3. Given a string, count the number of words in it. Ignore the case of characters. Also, consider that words are separated by one or more spaces.
<jupyter_code>
