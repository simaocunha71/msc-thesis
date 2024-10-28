
    def iscube(a):
        cube_root = round(a ** (1. / 3.))
        return cube_root ** 3 == a

    print(iscube(1))
    print(iscube(2))
    print(iscube(-1))
    print(iscube(64))
    print(iscube(0))
    print(iscube(180))

The function works by first calculating the cube root of the input integer (rounded to the nearest integer). Then it checks if the cube of this root equals the original input. If they are equal, it means the input is a perfect cube, so the function returns True. Otherwise, it returns False. This approach works because the cube of an integer n is n * n * n.

Note: For negative numbers, it still works because the cube root of a negative number is still a negative number, and it still satisfies the condition that cube of cube root equals the original number.
'''

# ---------------------------------SOLUTION----------------------------------

def iscube(n):
    n = abs(n)
    return round(n ** (1. / 3.)) ** 3 == n

# ---------------------------------TESTING----------------------------------

print(iscube(1))   # True
print(iscube(2))   # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))   # True
print(iscube(180)) # False

# ---------------------------------END---------------------------------------

'''
The function first takes the absolute value of the input to handle negative numbers. Then it computes the cube root of the input (rounded to the nearest integer), and checks if the cube of this root equals the original input. If they are equal, the function returns True, otherwise it returns False.
'''
<jupyter_output>
True
False
True
True
True
False
<jupyter_text>
Question 3:
<jupyter_code>
'''
