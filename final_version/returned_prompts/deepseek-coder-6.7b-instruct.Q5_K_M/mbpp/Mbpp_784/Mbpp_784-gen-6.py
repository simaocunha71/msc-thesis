def mul_even_odd(lst):
    even, odd = 1, 1
    for i in lst:
        if i % 2 == 0:
            even *= i
        else:
            odd *= i
    return even, odd

print(mul_even_odd([1,3,5,7,4,1,6,8]))

# Output:
# (32, 1152)

# This program takes a list as input and finds the product of first even and odd numbers in the list.
# It iterates over the list and checks if each element is even or odd. If the element is even, it multiplies the current value of "even" with the element. If the element is odd, it multiplies the current value of "odd" with the element.
# Finally, it returns the product of the first even number and the product of the first odd numbers in the list.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
