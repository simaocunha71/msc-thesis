def unique_product(lst):
    unique_numbers = set(lst)
    product = 1
    for number in unique_numbers:
        product *= number
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))

"""
Explanation:
The function unique_product takes a list as input. It converts the list to a set to remove duplicate numbers. It then initializes a variable 'product' to 1 and multiplies each unique number to this product. Finally, it returns the product.
"""
<jupyter_output>
720000000
<jupyter_text>
Problem 6:
<jupyter_code>
