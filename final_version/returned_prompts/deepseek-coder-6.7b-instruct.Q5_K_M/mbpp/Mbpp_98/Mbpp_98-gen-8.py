def multiply_num(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product / len(numbers)

# test case
print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

# Expected output: True
# This function works by initializing a variable "product" as 1. It then multiplies this product by every number in the input tuple, then divides by the length of the tuple to compute the average. The result is then compared to the expected output using math.isclose.
<jupyter_output>
True
<jupyter_text>
Exercise 3
<jupyter_code>
