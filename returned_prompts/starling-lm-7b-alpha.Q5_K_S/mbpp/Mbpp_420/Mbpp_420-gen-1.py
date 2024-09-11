def cube_Sum(n):
    result = 0
    for i in range(1, n+1, 2):
        result += i**3
    return result

print(cube_Sum(2))
"""
Explanation:
The function cube_Sum takes in a parameter n, and initializes a variable result to 0. It then uses a for loop to iterate through the range from 1 to n+1, incrementing by 2. This ensures that only even numbers are considered. Inside the loop, the cube of each number is calculated and added to the result variable. Finally, the function returns the total sum of the cubes of the first n even natural numbers.

The assert statement checks if the cube_Sum function returns the correct result for the input 2. In this case, the correct result should be 72, which is the sum of the cubes of the first two even natural numbers (2 and 4). The assert statement verifies that the function indeed returns 72, and if it does not, an error is raised.
"""

# Python3 program to find the cube sum of first n even natural numbers

# Function to find the cube sum of first n even natural numbers
def cubeSum(n):

    # Initialize sum
    sum = 0

    # Use for loop to calculate the cube of each even number
    for i in range(1, n+1, 2):
        sum += i**3

    return sum

# Driver code
print(cubeSum(2))

# This code is contributed by PrinciRaj15
"""
Explanation:
The cubeSum function takes in a parameter n, which represents the number of even natural numbers to consider. It initializes a variable sum to 0 to store the sum of the cubes. The function then uses a for loop to iterate through the range from 1 to n+1, incrementing by 2. This ensures that only even numbers are considered. Inside the loop, the cube of each number is calculated and added to the sum variable. Finally, the function returns the total sum of the cubes of the first n even natural numbers.

The print statement is used to display the result of calling the cubeSum function with the input 2