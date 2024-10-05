
    even_count = 0
    odd_count = 0
    
    num = abs(num)
    num = str(num)
    
    for digit in num:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return (even_count, odd_count)

print(even_odd_count(-12))
print(even_odd_count(123))
print(even_odd_count(1234567890))

Output:

(1, 1)
(1, 2)
(5, 5)

This code works by first converting the absolute value of the input number to a string, so that we can iterate over each digit. For each digit, it checks if the digit is even by converting it back to an integer and checking if the remainder of division by 2 is 0. If it is, it increments the even count; otherwise, it increments the odd count. The final counts are returned as a tuple.

This code has a time complexity of O(n), where n is the number of digits in the input number, because it performs a constant amount of work for each digit. It also has a space complexity of O(1), because it only uses a constant amount of space to store the counts and the input number.

This code works correctly for any integer input, including negative integers.
"""

# Solution 2:

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

print(even_odd_count(-12))
print(even_odd_count(123))
print(even_odd_count(1234567890))

# Solution 3:

def even_odd_count(num):
    even_count = sum(1 for digit in str(abs(num)) if int(digit) %