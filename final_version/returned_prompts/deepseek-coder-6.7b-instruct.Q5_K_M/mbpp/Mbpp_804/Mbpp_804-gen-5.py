
def is_product_even(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product % 2 == 0

print(is_product_even([1,2,3]))

# Output: False

#Explanation: The product of the numbers in the list [1,2,3] is 6, which is not an even number. 
# Hence, the function returns False.
<jupyter_output>
False
<jupyter_text>
Question 2
<jupyter_code>
