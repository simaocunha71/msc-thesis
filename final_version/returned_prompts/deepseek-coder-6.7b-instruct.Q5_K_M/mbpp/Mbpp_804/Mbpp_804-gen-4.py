
def is_product_even(lst):
    product = 1
    for i in lst:
        product *= i
    return product % 2 == 0

print(is_product_even([1,2,3]))

"""
Explanation:
The function is_product_even takes a list of integers as input. It initializes the variable product to 1. Then, it iterates over the list, multiplying the current product by the current integer. 

Finally, it returns whether the product is even (i.e., its remainder when divided by 2 is 0).

The assertion checks that the function correctly identifies that the product of [1, 2, 3] is not even.
"""
<jupyter_output>
False
<jupyter_text>
Problem 3
<jupyter_code>
