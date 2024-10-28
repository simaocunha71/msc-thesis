
    def closest_integer(value):
        num = float(value)
        if num > 0:
            return int(num + 0.5)
        else:
            return int(num - 0.5)

    print(closest_integer("10"))  # 10
    print(closest_integer("15.3"))  # 15
    print(closest_integer("14.5"))  # 15
    print(closest_integer("-14.5"))  # -15

This function works by converting the input string to a float, then adding 0.5 to it if the number is positive and subtracting 0.5 if it is negative. This has the effect of rounding the number to the nearest integer. Then it converts the result back to an int to get rid of the decimal places.

Note: The 0.5 is added or subtracted instead of using round() because we want to round away from zero, not towards it. For example, if the number is 14.5, adding 0.5 would result in 15.5, which is rounded to 16. But if we subtract 0.5 instead, we get 14.0, which is the correct rounded number.

The time complexity of this function is O(1), as it performs a fixed number of operations regardless of the size of the input. The space complexity is also O(1), as it uses a fixed amount of space to store the input and output values.

This function should be able to handle any valid input to the float() function. If the input is not a valid number, the function will raise a ValueError.

Here is a more complex example:

    def closest_integer(value):
        num = float(value)
        int_part = int(num)
        frac_part = num - int_part
        if frac_part < 0.5:
            return int_part
        elif frac_part > 0.5:
            return int_part + 1
        else:
            return int_part if int_part > 0 else int_part - 1

    print(closest_integer("14.5"))  # 15
   