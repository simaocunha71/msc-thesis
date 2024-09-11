def divisible_by_digits(startnum, endnum):
    def divisible_by_digit(num):
        num_str = str(num)
        for d in num_str:
            if num % int(d) != 0:
                return False
        return True
    return list(range(startnum, endnum + 1))[:filter(divisible_by_digit, range(startnum, endnum + 1))]

# assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
The function divisible_by_digits takes two integer parameters startnum and endnum and returns a list of numbers from startnum to endnum (inclusive). The function divisible_by_digit is defined as an inner function to check if a number is divisible by all of its digits. The divisible_by_digit function is applied to the range of numbers from startnum to endnum using the filter function to filter out numbers that are not divisible by all of their digits. The resulting list of numbers is returned as the output of divisible_by_digits.
"""

# Testing the function
assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
print("All test cases pass")











"""
The function divisible_by_digits is defined to take two integer parameters startnum and endnum. It returns a list of numbers from startnum to endnum (inclusive) that are divisible by all of their digits. 

To achieve this, the function defines an inner function called divisible_by_digit, which takes a number as input and checks if the number is divisible by all of its digits. This is done by converting the number to a string, iterating over each digit, and checking if the number modulo the digit is zero. If any