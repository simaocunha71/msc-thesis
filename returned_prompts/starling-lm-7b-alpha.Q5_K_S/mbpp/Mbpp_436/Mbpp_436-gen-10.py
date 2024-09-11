def neg_nos(lis):
    return [num for num in lis if num < 0]

# Test
print(neg_nos([-1,4,5,-6])) # returns [-1, -6]


























"""

Write a python function to return the negative numbers in a list.

Explanation

In this explanation, we will explain the code provided in the question.

The function neg_nos takes a list of numbers as an argument. It uses a list comprehension to create a new list that only contains the negative numbers. The condition num < 0 is used to filter out the negative numbers. The function returns the new list.

The assert statement is used to verify if the function is correct. It checks if the function returns the correct result for the given list [-1,4,5,-6]. If the assert statement is true, it means that the function is correct. Otherwise, an error message will be raised.

The print statement is used to test the function. It calls the function with the list [-1,4,5,-6] as an argument and prints the result. The output should be [-1, -6], which means that the function correctly identified the negative numbers in the list.

"""

"""

Explanation

In this explanation, we will explain the code provided in the question.

The function neg_nos takes a list of numbers as an argument. It uses a for loop to iterate over each number in the list. The condition num < 0 is used to check if the number is negative. If the condition is true, the number is added to the result list using the append method. The function returns the result list.

The assert statement is used to verify if the function is correct. It checks if the function returns the correct result for the given list [-1,4,5,-6]. If the assert statement is true, it means that the function is correct. Otherwise, an error message will be raised.

The print statement is used to test the function. It calls the function with the list [-1,4,5,-6] as an argument and prints the result. The output should be [-1, -6], which means that the function correctly identified the negative numbers in the