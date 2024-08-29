
def find_Parity(num):
    """
    This function takes an integer as input and returns True if the parity (number of 1s in binary representation) of the 
    given number is odd, else it returns False.
    """
    binary_num = bin(num)[2:] # binary representation of num
    ones_count = binary_num.count('1') # count of 1s in binary_num
    return ones_count % 2 != 0 # returns True if ones_count is odd else False

# Testing the function
print(find_Parity(12)) # should return False

"""
The bin() function is a built-in python function that converts an integer number to a binary string. 
The [2:] in the bin(num) is used to slice off the '0b' that python adds to the start of the binary string representation.
The count('1') function counts the number of 1s in the binary representation of the number.
The return statement checks if the count of 1s is odd by checking if the remainder when divided by 2 is not equal to 0.
If the remainder is not equal to 0, that means the count of 1s is odd and the function returns True.
Otherwise, the function returns False.
"""
<jupyter_output>
False
<jupyter_text>
Question 2
<jupyter_code>
