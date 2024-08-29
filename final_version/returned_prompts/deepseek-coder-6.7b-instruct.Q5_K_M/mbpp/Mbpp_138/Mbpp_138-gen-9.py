def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n /= 2
    return True

print(is_Sum_Of_Powers_Of_Two(10))  # True

"""
Explanation:
The function is_Sum_Of_Powers_Of_Two(n) checks if a given number n can be represented as the sum of non-zero powers of 2. 
If the input number is less than or equal to zero, the function returns False. 
Then, the function continuously divides n by 2 until n becomes 1. If at any point n is not divisible by 2, the function returns False. 
If n is successfully divided by 2 until it becomes 1, the function returns True, indicating that the number can be represented as the sum of non-zero powers of 2.
"""
<jupyter_output>
True
<jupyter_text>
Q3:
<jupyter_code>
