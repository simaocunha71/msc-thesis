
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg).replace("0b", "")

print(rounded_avg(1, 5))  # "0b11"
print(rounded_avg(7, 5))  # -1
print(rounded_avg(10, 20))  # "0b1111"
print(rounded_avg(20, 33))  # "0b11010"

# Solution by using the built-in Python functions round(), bin() and replace(). The function first checks if n is greater than m, if so it returns -1. Otherwise, it calculates the rounded average of n and m. It then converts this average to binary and removes the "0b" prefix.
<jupyter_output>
<empty_output>
<jupyter_text>
2. Given a string s, write a function that returns the first repeating character in it. If there is no repeating character, return "_".
<jupyter_code>
