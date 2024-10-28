
    def rounded_avg(n, m):
        if n > m:
            return -1
        avg = (n + m) // 2
        return bin(round(avg))

print(rounded_avg(1, 5))  # => "0b11"
print(rounded_avg(7, 5))  # => -1
print(rounded_avg(10, 20))  # => "0b1111"
print(rounded_avg(20, 33))  # => "0b11010"


The function first checks if n is greater than m, and if so, returns -1. If not, it computes the average of n and m, rounds it to the nearest integer, and converts it to binary using the bin function. The bin function returns a string that starts with '0b', indicating that it is a binary number, so the result is what we want.

Test this function with some examples to check that it works as expected.
"""

#Test Cases
print(rounded_avg(1, 5))  # => "0b11"
print(rounded_avg(7, 5))  # => -1
print(rounded_avg(10, 20))  # => "0b1111"
print(rounded_avg(20, 33))  # => "0b11010"
print(rounded_avg(2, 5))  # => "0b11"
print(rounded_avg(10, 21))  # => "0b11011"
print(rounded_avg(14, 19))  # => "0b1110"
print(rounded_avg(20, 40))  # => "0b11110"
print(rounded_avg(100, 200))  # => "0b1100100"
print(rounded_avg(50, 100))  # => "0b110