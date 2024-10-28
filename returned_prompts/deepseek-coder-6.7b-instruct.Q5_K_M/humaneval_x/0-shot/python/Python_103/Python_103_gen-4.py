
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) // 2
    return bin(round(avg))

print(rounded_avg(1, 5))  # => "0b11"
print(rounded_avg(7, 5))  # => -1
print(rounded_avg(10, 20))  # => "0b1111"
print(rounded_avg(20, 33))  # => "0b11010"

The function first checks if n is greater than m. If it is, it returns -1. If not, it computes the average of n and m, rounds it to the nearest integer and converts it to binary.

The average is computed by adding n and m and then dividing by 2. The result is then converted to binary using the bin function. The result is a string that starts with "0b" to indicate it's in binary format.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 2:  Write a Python function named `reverse_string` that takes a string as a parameter and returns the reverse of that string.
<jupyter_code>
"""
