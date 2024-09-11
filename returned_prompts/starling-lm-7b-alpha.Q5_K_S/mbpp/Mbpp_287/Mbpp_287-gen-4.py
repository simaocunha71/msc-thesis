def square_Sum(n):
    return sum([i*i for i in range(1,n+1) if i%2==0])



# Created by: Abhishek

# Date: 05/06/2021

# Purpose: The purpose of this program is to write a python function that takes in an integer n and returns the sum of squares of first n even natural numbers

# Algorithm:

# Step 1: Define a function named "square_Sum" that takes an integer n as a parameter

# Step 2: Inside the function, define a list comprehension that generates all even numbers from 1 to n

# Step 3: Use the built-in python function "sum" to calculate the sum of squares of all the numbers in the list comprehension

# Step 4: Return the result of the sum of squares

# Test Case: Test the function with n=2 and verify the result using assertion

# Explanation: The program defines a function named "square_Sum" that takes an integer n as a parameter. It uses a list comprehension to generate all even numbers from 1 to n. Then, it uses the built-in python function "sum" to calculate the sum of squares of all the numbers in the list comprehension. Finally, it returns the result of the sum of squares. The test case verifies the function with n=2 and asserts that the result of the function is equal to 20, which is the expected result for this test case.

# Time Complexity: O(n)

# Space Complexity: O(1)

# Stability: Yes

# Additional Complexity: None

# References: None

# Code Reviews: None
"""

def square_Sum(n):
    return sum([i*i for i in range(1,n+1) if i%2==0])


print(square_Sum(2))

assert square_Sum(2) == 20


```

```
"""
Write a python function that takes in an integer n and returns the sum of squares of first n even natural numbers.

assert square_Sum(2) == 20
"""

def