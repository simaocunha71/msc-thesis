def sum_of_digits(lst):
    return sum(sum(int(i) for i in str(x)) for x in lst)  # or return sum(sum(int(digit) for digit in str(x)) for x in lst)

# test the function
print(sum_of_digits([10,2,56]))  # expected output: 14

# explanation:
# The function takes a list of integers as an argument.
# It iterates over each number in the list.
# For each number, it converts the number to a string, then iterates over each character (digit) in the string.
# It converts each character back to an integer and sums them all up.
# It then sums up these sums for all numbers in the list.
# The final result is the sum of the digits of each number in the list.  # or return sum(sum(int(digit) for digit in str(x)) for x in lst)  # explanation:
# The function takes a list of integers as an argument.
# It iterates over each number in the list.
# For each number, it converts the number to a string, then iterates over each character (digit) in the string.
# It converts each character back to an integer and sums them all up.
# It then sums up these sums for all numbers in the list.
# The final result is the sum of the digits of each number in the list.  # test the function
print(sum_of_digits([10,2,56]))  # expected output: 14

# explanation:
# The function takes a list of integers as an argument.
# It iterates over each number in the list.
# For each number, it converts the number to a string, then iterates over each character (digit) in the string.
# It converts each character back to an integer and sums them all up.
# It then sums up these sums for all numbers in the list.
# The final result is the sum of the digits of each number in the list.  # or return sum(sum(int(digit) for digit in str(x)) for x in lst)  # explanation:
# The function takes a list of integers as an argument.
# It iterates over each number in the list.
# For each number, it converts the number to a string, then iterates over each character (digit) in the string.
# It converts each character back to an integer and sums them all up.
# It then sums up these sums for all numbers in the list