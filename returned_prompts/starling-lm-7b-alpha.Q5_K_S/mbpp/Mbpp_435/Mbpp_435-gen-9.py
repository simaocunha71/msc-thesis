def last_Digit(n):
    if n < 10:
        return n
    else:
        return last_Digit(n % 10)

# Driver Program
print(last_Digit(123))













"""
In the given problem, we need to find the last digit of a given number.
We can write a recursive function to solve this problem.
The function takes a number as an argument and checks if the number is less than 10. If it is, it returns the number itself as the last digit. Otherwise, it recursively calls itself with the remainder of the number divided by 10.
This process continues until the number becomes less than 10, and the function returns the last digit.
In the driver program, we call the function with the number 123 and print the result, which is 3, as expected.
"""

"""
In the given problem, we need to find the last digit of a given number.
We can write a recursive function to solve this problem.
The function takes a number as an argument and checks if the number is less than 10. If it is, it returns the number itself as the last digit. Otherwise, it recursively calls itself with the remainder of the number divided by 10.
This process continues until the number becomes less than 10, and the function returns the last digit.
In the driver program, we call the function with the number 123 and print the result, which is 3, as expected.
"""

"""
In the given problem, we need to find the last digit of a given number.
We can write a recursive function to solve this problem.
The function takes a number as an argument and checks if the number is less than 10. If it is, it returns the number itself as the last digit. Otherwise, it recursively calls itself with the remainder of the number divided by 10.
This process continues until the number becomes less than 10, and the function returns the last digit.
In the driver program, we call the function with the number 123 and print the result, which is 3, as expected.
"""

"""
In the given problem, we need to find the last digit of a