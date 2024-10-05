
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg)

print(rounded_avg(1, 5))  # "0b11"
print(rounded_avg(7, 5))  # -1
print(rounded_avg(10, 20))  # "0b1111"
print(rounded_avg(20, 33))  # "0b11010"


"""
The function rounded_avg(n, m) first checks if n is greater than m. If so, it returns -1. 
If n is not greater than m, it computes the average of n and m (rounded to the nearest integer). 
It then converts this average to binary format using the bin() function and returns it.
"""
<jupyter_output>
0b11
-1
0b1111
0b11010
<jupyter_text>
Question 2
<jupyter_code>
