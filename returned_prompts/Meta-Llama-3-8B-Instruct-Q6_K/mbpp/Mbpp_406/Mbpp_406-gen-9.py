```
def find_Parity(n):
    return n % 2 != 0
``` 
Explanation:
The function `find_Parity` takes an integer `n` as an argument. It returns `True` if the parity of `n` is odd and `False` if the parity of `n` is even. The parity of a number is considered odd if the number is odd, and even if the number is even. In Python, the `%` operator returns the remainder of the division of the number before it by the number after it. If the remainder is 0, then the number is even. Otherwise, the number is odd.

The unit test `assert find_Parity(12) == False` is used to verify that the function correctly identifies the parity of the number 12 as even. The function should return `False` for this input because 12 is an even number. 

This function can be used to solve the problem because it correctly identifies the parity of a given number as odd or even. The unit test provided also verifies that the function works correctly for at least one input.  However, it is important to note that this function does not handle non-integer inputs. For example, if you pass a float or a string as an argument, the function will raise an error. You may want to add error handling to the function to handle such cases. 