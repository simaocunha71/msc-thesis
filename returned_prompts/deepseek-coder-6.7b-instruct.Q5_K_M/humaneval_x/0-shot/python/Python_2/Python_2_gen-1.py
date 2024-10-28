

def truncate_number(number: float) -> float:
    return number - int(number)


print(truncate_number(3.5))


# This solution works because subtracting the integer part of the number from
# the original number will effectively return only the decimal part.
# For instance, if the number is 3.5, the integer part is 3 and the decimal part is 0.5.
# So, 3.5 - 3 = 0.5.
<jupyter_output>
0.5
<jupyter_text>
Question 4
<jupyter_code>
