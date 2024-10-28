

def truncate_number(number: float) -> float:
    return number % 1

# Test cases
print(truncate_number(3.5))  # 0.5
print(truncate_number(10.7))  # 0.7
print(truncate_number(100.0))  # 0.0


# Alternative solution
def truncate_number(number: float) -> float:
    int_part = int(number)
    return number - int_part

# Test cases
print(truncate_number(3.5))  # 0.5
print(truncate_number(10.7))  # 0.7
print(truncate_number(100.0))  # 0.0

Both solutions work. The first one uses the modulus operator to get the decimal part of the number. The second solution uses the integer part of the number by casting the float to an integer using the int() function, then subtracts this from the original number to get the decimal part.
<jupyter_output>
<empty_output>
<jupyter_text>
4. Write a function in Python that takes a string and returns a new string with all the characters in lowercase.
<jupyter_code>
