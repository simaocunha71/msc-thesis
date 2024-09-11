def find_Average_Of_Cube(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total / n

# Testing the function
assert find_Average_Of_Cube(2) == 4.5, "Test case 1 failed"
print("All test cases passed")



def find_Average_Of_Cube(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total / n

# Testing the function
assert find_Average_Of_Cube(2) == 4.5, "Test case 1 failed"
print("All test cases passed")


"""
To check if the function is correctly working or not, we can add some test cases. Here, we have added one test case for checking the function. The test case is to check if the function returns the correct result for the input 2. The correct result for the input 2 is 4.5. If the function returns 4.5 for the input 2, then the test case passes. Otherwise, the test case fails.
"""

"""
In this code, we define a function find_Average_Of_Cube that takes a number n as input and returns the average of cubes of first n natural numbers. The function initializes a variable total to 0. Then, it uses a for loop to iterate over the range from 1 to n + 1. Inside the loop, it adds the cube of each number i to the total. Finally, it returns the total divided by n.
"""

"""
To find the average of cubes of first n natural numbers, we can use the formula:

sum(i^3 for i in range(1, n + 1)) / n

In the function find_Average_Of_Cube, we use a for loop to iterate over the range from 1 to n + 1. Inside the loop, we calculate the cube of each number i and add it to the total. After the loop, we return the total divided by n. This gives us the average of cubes of first n natural numbers.
"""

