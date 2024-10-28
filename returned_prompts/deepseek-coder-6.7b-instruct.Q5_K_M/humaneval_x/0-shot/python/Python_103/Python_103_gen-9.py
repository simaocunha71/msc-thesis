
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg)

# Test cases
print(rounded_avg(1, 5))  # => "0b11"
print(rounded_avg(7, 5))  # => -1
print(rounded_avg(10, 20))  # => "0b1111"
print(rounded_avg(20, 33))  # => "0b11010"
<jupyter_output>
0b11
-1
0b1111
0b11010
<jupyter_text>
Problem 2:
<jupyter_code>
