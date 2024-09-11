def difference(n):
    return sum([i**3 for i in range(1,n+1)]) - sum(range(1,n+1))

# Testing the function
print(difference(3))
# Output: 30








"""
Explanation:
In the above code, we defined a function named 'difference' that takes an input parameter 'n'. The function calculates the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers using list comprehension and built-in functions in Python.

The function uses a list comprehension to generate a list of cubes of the first n natural numbers, i.e., [i**3 for i in range(1,n+1)]. Then, it uses the built-in function 'sum' to calculate the sum of the cubes of the first n natural numbers.

Similarly, the function uses another list comprehension to generate a list of the first n natural numbers, i.e., [i for i in range(1,n+1)]. Then, it uses the built-in function 'sum' to calculate the sum of the first n natural numbers.

Finally, the function subtracts the sum of the cubes of the first n natural numbers from the sum of the first n natural numbers to obtain the desired difference.

In the test case, we called the function with the argument 3 and printed the result, which is 30.
"""

"""
Explanation:
In the given Python function, the purpose is to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.

To achieve this, the function uses two list comprehensions. The first one generates a list of cubes of the first n natural numbers, and the second one generates a list of the first n natural numbers. Then, the function uses the built-in 'sum' function to calculate the sum of these two lists.

Finally, the function subtracts the sum of the cubes of the first n natural numbers from the sum of the first n natural numbers to obtain the desired difference.

The function is tested with the argument 3, and the result is printed, which is 30.
"""

"""
