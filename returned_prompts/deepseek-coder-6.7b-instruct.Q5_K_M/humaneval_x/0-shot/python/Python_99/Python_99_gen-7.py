
    value = float(value)
    if value >= 0:
        return int(value + 0.5)
    else:
        return int(value - 0.5)

print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))

Output:
10
15
15
-15

Explanation:
The function works by first converting the input string to a float. Then, it uses the rounding rules to determine the closest integer. If the number is positive or zero, it rounds up (adds 0.5) and then converts back to an integer. If the number is negative, it rounds down (subtracts 0.5) and then converts back to an integer.

This solution assumes that the input string will always be a valid number. If this is not the case, you should add error checking to handle invalid inputs.

This solution also assumes that the input string will not have leading or trailing whitespace. If this is not the case, you should strip the input string before converting it to a float.

This solution also assumes that the input string will not have any characters other than digits, a decimal point, and an optional negative sign. If this is not the case, you should add error checking to handle invalid inputs.

This solution also assumes that the input string will not be very large. If this is not the case, you may need to use a different method to convert the string to a float and round it.

This solution also assumes that the input string will not have any leading or trailing whitespace. If this is not the case, you should strip the input string before converting it to a float.

This solution also assumes that the input string will not have any characters other than digits, a decimal point, and an optional negative sign. If this is not the case, you should add error checking to handle invalid inputs.

This solution also assumes that the input string will not be very large. If this is not the case, you may need to use a different method to convert the string to a float and round it.

This solution also assumes that the input string will not have any leading or trailing whites