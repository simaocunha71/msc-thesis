def is_Sum_Of_Powers_Of_Two(n):
    # Base case
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True

    # Initialize starting value to 2^0
    power = 0
    while 2 ** power <= n:
        if is_Sum_Of_Powers_Of_Two(n - 2 ** power):
            return True
        power += 1

    return False

# Test the function
print(is_Sum_Of_Powers_Of_Two(10))
assert is_Sum_Of_Powers_Of_Two(10) == True
<jupyter_output>
True
<jupyter_text>
Problem 5: Write a python function to calculate the sum of the numbers in a list until the sum is less than or equal to a given target number.
<jupyter_code>
