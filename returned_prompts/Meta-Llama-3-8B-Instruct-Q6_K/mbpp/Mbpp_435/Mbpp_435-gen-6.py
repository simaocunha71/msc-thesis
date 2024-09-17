"""
The problem is asking for a function that takes an integer as input and returns the last digit of that integer. 

However, the problem statement doesn't specify the type of the input. It could be an integer or a string. 

Luckily, the unit test `assert last_Digit(123) == 3` suggests that the input will be an integer. 

So, we can write a simple function that uses the modulus operator to find the last digit of the input number. Here is the solution:
"""

def last_Digit(n):
    return n % 10
"""
This function takes an integer `n` as input, and returns the remainder of `n` divided by 10. This remainder is the last digit of the number. For example, if `n` is 123, `n % 10` will be 3.  """



