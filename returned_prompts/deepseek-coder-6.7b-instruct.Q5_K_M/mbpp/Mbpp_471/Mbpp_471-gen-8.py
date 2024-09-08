def find_remainder(lst, n):
    product = 1
    for i in lst:
        product = (product * i) % n
    return product

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11))

# Output: 9

# Explanation:
# The function first initializes the variable product to 1, which will store the running product of all elements in the list.
# Then, for each element in the list, it multiplies the current product by the element, and takes the remainder of the division by n.
# This is done because the remainder of the division of two numbers is always less than the divisor.
# So, this operation effectively 'reduces' the product to its remainder when divided by n.
# Finally, it returns the product.
# In the given example, the function multiplies the numbers 100, 10, 5, 25, 35, and 14 together, then takes the remainder when divided by 11.
# The result is 9, so the function returns this.
<jupyter_output>
9
<jupyter_text>
Problem 2
<jupyter_code>
