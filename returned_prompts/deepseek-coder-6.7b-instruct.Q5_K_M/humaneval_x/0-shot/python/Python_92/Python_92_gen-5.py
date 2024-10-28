
def any_int(x, y, z):
    if x == int(x) and y == int(y) and z == int(z):
        if x == y + z or y == x + z or z == x + y:
            return True
    return False

print(any_int(5, 2, 7)) #➞ True
print(any_int(3, 2, 2)) #➞ False
print(any_int(3, -2, 1)) #➞ True
print(any_int(3.6, -2.2, 2)) #➞ False
print(any_int(3, 2.5, 4)) #➞ False
print(any_int(4, 4, 4)) #➞ True


# The function first checks if all inputs are integers, if not it returns False.
# Then it checks if any of the inputs is equal to the sum of the other two inputs.
# If either condition is met it returns True, otherwise it returns False.

# Note: In the question, it's stated that we are considering integer values only. So, we are using int() to check whether the numbers are integers or not.
<jupyter_output>
True
False
True
False
False
True
<jupyter_text>
