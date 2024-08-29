def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0

print(is_product_even([1,2,3]))
<jupyter_output>
False
<jupyter_text>
Question 2
<jupyter_code>
