
    binary = bin(decimal).replace("0b","")
    return 'db' + binary + 'db'

# Test cases
print(decimal_to_binary(15)) # should return "db1111db"
print(decimal_to_binary(32)) # should return "db100000db"
print(decimal_to_binary(255)) # should return "db1111111db"
print(decimal_to_binary(0)) # should return "db0db"

In this code, we use the built-in function bin() to convert the decimal number to a binary string. The bin() function returns a string that starts with "0b" to indicate that it is a binary number, so we use the replace() function to remove "0b". We then add the extra "db" characters at the beginning and end of the string.

This function works for any non-negative integer input. If the input is negative, the bin() function will return a string that starts with "-0b", so we won't be able to remove the "0b" part with replace(). The problem statement says that the input will be a non-negative integer, so this case is not covered by the code.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
