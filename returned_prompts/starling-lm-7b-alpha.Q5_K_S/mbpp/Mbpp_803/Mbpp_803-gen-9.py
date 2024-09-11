def is_perfect_square(n):
    root = int(n**0.5)
    return root*root == n

# test
assert is_perfect_square(1) == True
assert is_perfect_square(4) == True
assert is_perfect_square(9) == True
assert is_perfect_square(10) == False
assert is_perfect_square(25) == True

# assert is_perfect_square(10) == False

"""
Explanation:
To determine whether a number is a perfect square or not, we can calculate the square root of the number. 
If the square root is an integer, then the number is a perfect square. 
In this function, we first calculate the square root of the number and convert it to an integer using the int() function. 
Then we check if the square of the integer is equal to the number. 
If the square is equal to the number, then the number is a perfect square; otherwise, it is not.
"""

# Python3 program to check if a number is a
# perfect square or not

# Function to check if a number is perfect
# square or not
def isPerfectSquare(x):
    # Find floating point value of
    # square root of x.
    sr = x ** 0.5

    # If square root is an integer
    # then check if (x/sr) is an
    # integer, then x is a perfect
    # square else not
    return ((sr - int(sr)) == 0)

# Driver program to test above function
x = 4
if (isPerfectSquare(x)):
    print("Yes")
else:
    print("No")

# This code is contributed by PrinciRaj13
```
