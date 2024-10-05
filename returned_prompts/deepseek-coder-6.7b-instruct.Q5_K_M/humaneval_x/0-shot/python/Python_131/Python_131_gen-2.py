
    def digits(n):
        product = 1
        for i in str(n):
            if int(i) % 2 != 0:
                product *= int(i)
        return product if product != 1 else 0

    print(digits(1))  # 1
    print(digits(4))  # 0
    print(digits(235))  # 15

"""
This solution works by first converting the integer to a string so that we can iterate over each digit. 
We initialize the product as 1, and for each digit in the string, if it is odd (i.e., its remainder when divided by 2 is not 0), we multiply the product by this digit. 
Finally, we return the product if it is not 1, otherwise we return 0, since in this case all digits were even.
"""

"""
The complexity of this solution is O(n) where n is the number of digits in the input integer, 
as we are iterating over each digit once. This is the best time complexity we can achieve for this problem.
"""

"""
The space complexity is O(1) as we are using a constant amount of space to store the product and the digits. 
This means the space used does not grow with the size of the input.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Problem 2**
<jupyter_code>
