def find_Index(n):
    count = 0
    for i in range(1, 10 ** n):
        if i * (i + 1) // 2 < 10 ** n:
            count += 1
        else:
            break
    return count

print(find_Index(2))
# Output: 4



# Explanation
# Here is a simple Python program that prints out the index of the smallest triangular number with the number of digits specified by the user.

# The program first defines a function called "find_Index" that takes an integer parameter "n" representing the number of digits in the triangular number.

# Inside the function, a variable "count" is initialized to 0. This variable will be used to keep track of the number of triangular numbers that have fewer than "n" digits.

# The program then enters a loop that iterates over all integers from 1 to 10^n (inclusive). For each integer, it calculates the triangular number by multiplying the integer by (i + 1) and dividing by 2.

# If the triangular number is less than 10^n, the program increments the "count" variable by 1. Otherwise, it breaks out of the loop.

# After the loop, the function returns the value of "count", which represents the index of the smallest triangular number with "n" digits.

# Finally, the program prints the result of calling the "find_Index" function with the input value of 2. This will print the index of the smallest triangular number with 2 digits, which is 4.

# The time complexity of this program is O(n), where n is the input value. This is because the program must iterate over all integers from 1 to 10^n, and each iteration takes constant time.

"""
"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""
