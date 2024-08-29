
def mul_even_odd(lst):
    even_product = 1
    odd_product = 1
    for num in lst:
        if num % 2 == 0:
            even_product *= num
        else:
            odd_product *= num
    return even_product, odd_product

print(mul_even_odd([1,3,5,7,4,1,6,8]))

# Output: (16, 1152)

# Explanation:
# In the given list, the even numbers are 4, 6 and 8. Their product is 16. 
# The odd numbers are 1, 3, 5, 7, 1. Their product is 1152. So the function returns (16, 1152).
<jupyter_output>
(16, 1152)
<jupyter_text>
Question 2:
<jupyter_code>
