
def closest_integer(value):
    num = float(value)
    if num > 0:
        return int(num + 0.5)
    else:
        return int(num - 0.5)

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))

print(int(14.5 + 0.5))
print(int(-14.5 - 0.5))

"""
The function closest_integer takes in a string representing a number. It first converts the string to a float. Then, it checks if the float is positive or negative. If it's positive, it rounds the float up by adding 0.5 and then converts back to an integer. If it's negative, it rounds the float down by subtracting 0.5 and then converts back to an integer. This results in the closest integer to the original float.
"""

# Test cases
assert closest_integer("10") == 10
assert closest_integer("15.3") == 15
assert closest_integer("14.5") == 15
assert closest_integer("-14.5") == -15

# Test cases
assert closest_integer("10") == 10
assert closest_integer("15.3") == 15
assert closest_integer("14.5") == 15
assert closest_integer("-14.5") == -15
print("All test cases pass")
<jupyter_output>
10
15
15
-15
15
-15
All test cases pass
<jupyter_text>
Exercise 2: Write a Python function that takes two strings as arguments and returns a string which is the concatenation of the two arguments.
<jupyter_code>
# Code:

def concat_two_strings(str1, str2):
    return str1 + str2

# Test cases
assert concat_two_strings("Hello, ", "World") == "Hello, World"
assert concat_two_strings("