# Here's a step-by-step breakdown of the code:

# First, we import the math module to use the ceil function.
import math

# Next, we define the sum_squares function that takes a list as its parameter.
def sum_squares(lst):
    # We initialize a variable called sum_squares to 0. This variable will keep track of the sum of squared numbers in the list.
    sum_squares = 0

    # We iterate through each element in the list using a for loop.
    for elem in lst:
        # Inside the loop, we round each element in the list to the upper int (ceiling) using the math.ceil function.
        rounded_elem = math.ceil(elem)
        # Then, we square the rounded element by multiplying it by itself.
        squared_elem = rounded_elem ** 2
        # After that, we add the squared element to the sum_squares variable.
        sum_squares += squared_elem
    # Finally, we return the sum_squares variable as the result of the function.
    return sum_squares

# Here are some test cases to verify the correctness of the function:

# Test case 1: lst = [1,2,3]
print(sum_squares([1,2,3]))  # Expected output: 14

# Test case 2: lst = [1,4,9]
print(sum_squares([1,4,9]))  # Expected output: 98

# Test case 3: lst = [1,3,5,7]
print(sum_squares([1,3,5,7]))  # Expected output: 84

# Test case 4: lst = [1.4,4.2,0]
print(sum_squares([1.4,4.2,0]))  # Expected output: 29

# Test case 5: lst = [-2.4,1,1]
print(sum_squares([-2.4,1,1]))  # Expected output: 6