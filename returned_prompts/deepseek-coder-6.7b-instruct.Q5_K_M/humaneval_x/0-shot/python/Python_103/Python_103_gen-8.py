
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) // 2
    return bin(round(avg))

# test cases
print(rounded_avg(1, 5))  # => "0b11"
print(rounded_avg(7, 5))  # => -1
print(rounded_avg(10, 20))  # => "0b1111"
print(rounded_avg(20, 33))  # => "0b11010"

# The function works by first checking if n is greater than m. If so, it returns -1.
# Otherwise, it calculates the average of n and m rounded to the nearest integer.
# Finally, it converts this rounded average to binary using Python's built-in bin function and returns the result.
# The bin function prepends "0b" to the result to indicate that it is a binary number.

# The round function is used to round the average to the nearest integer.
# The "//" operator is used for integer division to calculate the average of n and m.
# The result is then converted to binary and returned.

# The result of the function is the binary representation of the rounded average of n and m.
# If n is greater than m, the function returns -1.
<jupyter_output>
0b11
-1
0b1111
0b11010
<jupyter_text>
Question 2:Write a Python program that reads a string and performs the following operations:1. Count the total number of alphabets in the string.2. Count the total number of digits in the string.3. Count the total number of white spaces in the string.4. Count the total number of other characters (special characters) in the string.5. Count the total number of lowercase letters in the string.6. Count the total number of uppercase letters in the string.7. Convert all the uppercase letters in the string to lowercase.8. Convert all the lowercase letters in the string to uppercase.9. Check if the string is a pal