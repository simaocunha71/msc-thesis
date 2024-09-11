def sum_of_digits(numbers):
    # Your code here
    result = 0
    for i in numbers:
        result += sum(map(int, str(i)))
    return result

# Testing
assert sum_of_digits([10,2,56]) == 14
print("All tests passed.")







"""
The task is to compute the sum of digits of each number of a given list.
To solve this, first convert the number to a string, and then use the map function to convert each character to an integer. Then, use the sum function to compute the sum of all digits. Finally, add the sum of digits of each number to the result.

The provided code defines a function called "sum_of_digits" that takes a list of numbers as input. Inside the function, an initial variable called "result" is set to 0. Then, a for loop iterates over each number in the input list. For each number, the string representation of the number is converted to a list of integers using the map function. The sum of these integers is computed using the sum function, and added to the "result" variable. After processing all numbers in the input list, the function returns the final value of "result".

To test the function, the provided assert statement is used to verify if the function correctly computes the sum of digits for the given input list [10,2,56]. If the assert statement passes, the message "All tests passed." is printed, indicating that the function is working correctly. Otherwise, an error message is raised.
"""

"""
In this code, the function sum_of_digits is defined to calculate the sum of digits of each number in a given list. The function uses a loop to iterate through each number in the list. For each number, it converts the number to a string using the str() function. Then, it uses the map() function to convert each character in the string representation of the number to an integer. The sum() function is used to calculate the sum of these integers, which represents the sum of digits of the original number. Finally, the sum of digits for each number in the list is added to the result variable. The function returns the final result.

To test the function,