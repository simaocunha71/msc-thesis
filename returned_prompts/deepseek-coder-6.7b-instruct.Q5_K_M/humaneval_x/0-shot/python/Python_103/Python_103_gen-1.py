
    if n > m:
        return -1
    else:
        avg = (n + m) // 2
        return bin(avg)

# Test the function
print(rounded_avg(1, 5))  # => "0b11"
print(rounded_avg(7, 5))  # => -1
print(rounded_avg(10, 20))  # => "0b1111"
print(rounded_avg(20, 33))  # => "0b11010"

# The test cases are correct, and the function is working as expected.
<jupyter_output>
0b11
-1
0b1111
0b11010
<jupyter_text>
Problem 2:
<jupyter_code>
