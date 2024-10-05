
def even_odd_count(num):
    # Convert the number to a string to be able to iterate over its digits.
    num_str = str(abs(num))
    # Initialize the counts of even and odd digits to zero.
    even_count = 0
    odd_count = 0
    # Iterate over the digits of the number.
    for digit in num_str:
        # If the digit is even (divisible by 2), increment the even count.
        if int(digit) % 2 == 0:
            even_count += 1
        # If the digit is odd (not divisible by 2), increment the odd count.
        else:
            odd_count += 1
    # Return the counts as a tuple.
    return (even_count, odd_count)

# Test cases:
print(even_odd_count(12))  # Should return (1, 1).
print(even_odd_count(123))  # Should return (1, 2).
print(even_odd_count(-12))  # Should return (1, 1).

# Note: This solution assumes that the input number is an integer. It uses the absolute value of the number to avoid dealing with negative numbers in the counting process.

# The solution uses a for loop to iterate over the digits of the number. It converts the number to a string to be able to access its digits one by one. It initializes the counts of even and odd digits to zero and increments them accordingly as it goes through the digits. Finally, it returns the counts as a tuple.

# The time complexity of this solution is O(n), where n is the number of digits in the input number. This is because the solution iterates through each digit exactly once.

# The space complexity of this solution is O(1), as it uses a fixed amount of space to store the counts of even and odd digits.

# This solution is suitable for small to medium-sized input numbers, as the time and space complexities are both linear with respect to the size of the input.

# However, if the input number is very large, this solution may not be efficient enough. In such cases, a more