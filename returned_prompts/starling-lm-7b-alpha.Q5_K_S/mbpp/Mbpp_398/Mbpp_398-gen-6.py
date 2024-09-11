"""
To solve this, we can use the following steps:

1. Define a function called sum_of_digits that takes a list as an argument.
2. Inside the function, initialize a variable called total_sum to 0. This variable will keep track of the sum of the digits of each number in the list.
3. Use a for loop to iterate over each number in the list.
4. Inside the loop, convert each number to a string using the str() function to enable easier manipulation of the digits.
5. Use a for loop to iterate over each digit in the string representation of the number.
6. Convert each digit to an integer using the int() function, and add it to the total_sum variable.
7. After the inner loop finishes, move to the next number in the outer loop.
8. Repeat steps 5-7 until all numbers in the list have been processed.
9. Finally, return the total_sum variable as the result of the function.

Here is the code for the solution:

def sum_of_digits(numbers):
    total_sum = 0
    for num in numbers:
        str_num = str(num)
        for digit in str_num:
            total_sum += int(digit)
    return total_sum
"""

# Test
assert sum_of_digits([10,2,56])==14

# Explanation:
# The function sum_of_digits takes a list of numbers as an argument. It initializes a variable called total_sum to 0, which will keep track of the sum of the digits of each number in the list.
# It then uses a for loop to iterate over each number in the list. Inside the loop, it converts each number to a string using the str() function. This is necessary because strings are iterable in Python, which allows us to easily access each digit of the number.
# Next, it uses another for loop to iterate over each digit in the string representation of the number. Inside this loop, it converts each digit to an integer using the int() function, and adds it to the total_sum variable.
# After the inner loop finishes, it moves on to the next number in the outer loop and repeats the