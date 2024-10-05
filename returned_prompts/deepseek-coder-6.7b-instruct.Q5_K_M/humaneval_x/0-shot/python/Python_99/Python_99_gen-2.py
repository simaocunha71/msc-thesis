
    value = float(value)
    if value < 0:
        return int(value) if abs(value - int(value)) < 0.5 else int(value) - 1
    else:
        return int(value) if abs(value - int(value)) < 0.5 else int(value) + 1


print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))

# Output:
# 10
# 15
# 15
# -15

# Note:
# The function works by first converting the input string to a float. Then it checks if the float is negative. If it is, it compares the absolute difference between the float and its integer part to 0.5. If the difference is less than 0.5, it returns the integer part of the float. If the difference is 0.5 or greater, it subtracts 1 from the integer part of the float. If the float is not negative, it does the same thing except it adds 1 to the integer part instead of subtracting.
# This is because in Python, the "//" operator is used for integer division, which truncates the decimal part of a number. Therefore, if the float is equidistant from two integers, the one that is returned is the one that is the farthest from zero.
# This is also why the function uses the "abs" function to get the absolute difference between the float and its integer part. The "abs" function returns the magnitude of a number without considering its sign.
# The function finally returns the result as an integer using the "int" function. The "int" function truncates the decimal part of a number and returns the integer part.
# This way, the function can correctly return the closest integer to any given float.
<jupyter_output>
10
15
15
-15
<jupyter_text>
Question 4
<jupyter_code>
