def dif_Square(n):
    j = 0
    while j*j <= n:
        i = 0
        while i*i <= n:
            if i*i + j*j == n:
                return True
            i += 1
        j += 1
    return False

print(dif_Square(5)) # True
print(dif_Square(10)) # True
print(dif_Square(11)) # False
print(dif_Square(12)) # True
print(dif_Square(13)) # False


"""
This function is checking all combinations of i*i and j*j where i and j are all numbers from 0 to sqrt(n).
If at any point the sum of i*i and j*j equals n, then n can be represented as the difference of two squares and the function returns True.
If no combination is found, then n cannot be represented as the difference of two squares and the function returns False.
"""


"""
Explanation:
The function dif_Square(n) takes an integer n as input and returns a boolean value.
The outer while loop runs from 0 to sqrt(n) and the inner while loop also runs from 0 to sqrt(n).
This is done to find all possible pairs of numbers i and j.
If i*i + j*j equals n, then n can be represented as the difference of two squares and the function returns True.
If no pair is found, then n cannot be represented as the difference of two squares and the function returns False.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a Python program to find the sum of the digits of a number.
<jupyter_code>
