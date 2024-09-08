
def find_Parity(n):
    return n % 2 != 0

print(find_Parity(12)) # False

# The function find_Parity works by using the modulus operator to get the remainder of the division of n by 2. If the remainder is not 0, it means that n is not divisible by 2 and therefore, the parity of the number is odd.

# The assert statement checks if the function find_Parity(12) returns False which is the expected output. If not, the program will throw an AssertionError.
<jupyter_output>
False
<jupyter_text>
Question 2:
<jupyter_code>
