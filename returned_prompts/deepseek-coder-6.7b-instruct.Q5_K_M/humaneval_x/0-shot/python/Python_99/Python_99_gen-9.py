
    value = float(value)
    if value > 0:
        return int(value) + 1 if value - int(value) >= 0.5 else int(value)
    else:
        return int(value) - 1 if int(value) - value >= 0.5 else int(value)


print(closest_integer("10"))
print(closest_integer("15.3"))
print(closest_integer("14.5"))
print(closest_integer("-14.5"))

In this function, we first convert the string to a float. Then we check if the value is greater than 0. If it is, we add 1 to the integer part of the value if the decimal part is 0.5 or greater, or keep the integer part if it's less than 0.5. If the value is less than 0, we subtract 1 from the integer part of the value if the decimal part is 0.5 or greater, or keep the integer part if it's less than 0.5. We then return this value.
<jupyter_output>
<empty_output>
<jupyter_text>
