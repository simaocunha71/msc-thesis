def count_Set_Bits(n):
    return bin(n).count("1")

print(count_Set_Bits(2))

# The function works by converting the number to binary using the built-in bin() function, then using the count() method to count the number of 1's in the binary representation.

# When run, this code should print 1, which is the number of set bits in the binary representation of 2 (0b10).
assert count_Set_Bits(2) == 1
# This assert statement checks that the function is working correctly. If the function returns the wrong result, it will raise an AssertionError.
<jupyter_output>
1
<jupyter_text>
Q2:
<jupyter_code>
