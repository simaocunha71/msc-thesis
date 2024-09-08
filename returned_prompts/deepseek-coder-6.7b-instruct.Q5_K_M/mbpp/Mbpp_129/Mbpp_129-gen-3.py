def magic_square_test(matrix):
    # calculate the sum of the first row
    magic_constant = sum(matrix[0])
    # check rows
    for row in matrix:
        if sum(row) != magic_constant:
            return False
    # check columns
    for col in range(len(matrix[0])):
        if sum(row[col] for row in matrix) != magic_constant:
            return False
    # check diagonals
    if sum(matrix[i][i] for i in range(len(matrix))) != magic_constant:
        return False
    if sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))) != magic_constant:
        return False
    return True

# test the function
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True
assert magic_square_test([[16, 3], [5, 11], [9, 7], [6, 10], [12, 4], [8, 2]])==False
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2: Write a Python program that will calculate the sum of the squares of the digits of a number.Example: For 345, the result will be 3^2 + 4^2 + 5^2 = 9 + 16 + 25 = 50
<jupyter_code>
def sum_of_squares(n):
    return sum(int(digit)**2 for digit in str(n))

# test the function
assert sum_of_squares(345) == 50
assert sum_of_squares(12) == 5
assert sum_of_squares(999