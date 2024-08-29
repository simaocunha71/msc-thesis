
def check_monthnumber_number(n):
    if n in [4, 6, 9, 11]:
        return True
    else:
        return False

print(check_monthnumber_number(6))
<jupyter_output>
True
<jupyter_text>
Problem 2:Write a function to check whether the given year is a leap year or not. The conditions for a leap year are as follows:* The year can be evenly divided by 4;* If the year can be evenly divided by 100, it is NOT a leap year, unless;* The year is also evenly divisible by 400. Then it is a leap year.
<jupyter_code>
