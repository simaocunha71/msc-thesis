def multiply_num(lst):
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)

print(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

# Expected output: True
<jupyter_output>
True
<jupyter_text>
Question 2:Write a function to calculate the sum of all the elements in a list. If the list is empty, the function should return 0.
<jupyter_code>
