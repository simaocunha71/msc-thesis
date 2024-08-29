def cube_nums(lst):
    return [i**3 for i in lst]

print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
<jupyter_output>
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
<jupyter_text>
Q2. Write a function to check if a number is even or odd.
<jupyter_code>
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(10))
print(even_odd(7))
<jupyter_output>
Even
Odd
<jupyter_text>
Q3. Write a function to convert a decimal number to binary.
<jupyter_code>
def dec_to_bin(n):
    return bin(n).replace("0b", "")

print(dec_to_bin(10))
print(dec_to_bin(7))
<jupyter_output>
1010
111
<jupyter_text>
Q4. Write a function to find the factorial of a number.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(3))
<jupyter_output>
120
6
<jupyter_text>
Q5. Write a function to find the square root of a number.
<jupyter_code>
import math

def square_root(n):
    return math.sqrt(n)

print(square_root(16))
print(square_root(15))
<jupyter_output>
4.0
