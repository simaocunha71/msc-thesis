
def is_product_even(lst):
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0

print(is_product_even([1,2,3]))
<jupyter_output>
False
<jupyter_text>
Exercise 2:Write a function that takes a list of numbers and returns a list with the square of those numbers.
<jupyter_code>
