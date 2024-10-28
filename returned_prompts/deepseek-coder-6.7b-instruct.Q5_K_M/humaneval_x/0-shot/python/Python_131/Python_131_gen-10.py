
    # initialize the product to 1
    product = 1

    # convert the number to a string to iterate over its digits
    n = str(n)

    # iterate over the digits
    for digit in n:
        # if the digit is odd, multiply the product by this digit
        if int(digit) % 2 != 0:
            product *= int(digit)

    # return the product
    return product

print(digits(235))
<jupyter_output>
15
<jupyter_text>
Question 3:
<jupyter_code>
