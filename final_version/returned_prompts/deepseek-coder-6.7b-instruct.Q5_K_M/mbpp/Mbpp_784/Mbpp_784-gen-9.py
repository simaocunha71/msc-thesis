
def mul_even_odd(lst):
    even = 1
    odd = 1
    for i in lst:
        if i % 2 == 0:
            even *= i
        else:
            odd *= i
    return even, odd

# Testing the function
even, odd = mul_even_odd([1,3,5,7,4,1,6,8])
print(even)
print(odd)
<jupyter_output>
32
32
<jupyter_text>
Question 2:
<jupyter_code>
