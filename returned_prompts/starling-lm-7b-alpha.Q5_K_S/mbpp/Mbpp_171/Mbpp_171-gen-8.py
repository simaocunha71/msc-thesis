"""
To calculate the perimeter of a regular pentagon, you can follow these steps:

1. Define a function called `perimeter_pentagon` that takes the number of sides (in this case, 5) as its input.
2. Inside the function, calculate the length of one side by dividing the total number of sides by the number of sides.
3. Multiply the length of one side by the total number of sides to find the perimeter.
4. Return the calculated perimeter.

Here's an example implementation in Python:

def perimeter_pentagon(sides):
    # Calculate the length of one side
    side_length = sides / sides
    # Calculate the perimeter
    perimeter = side_length * sides
    # Return the perimeter
    return perimeter

To test the function, you can call it with the number of sides as an argument and compare the result with the expected value. In this case, you can use the `assert` statement to check if the calculated perimeter is equal to the expected value of 25.

Here's an example usage of the function:

assert perimeter_pentagon(5) == 25
"""

def perimeter_pentagon(sides):
    side_length = sides / sides
    perimeter = side_length * sides
    return perimeter

# Test the function
assert perimeter_pentagon(5) == 25

# Test with different number of sides
print(perimeter_pentagon(6))  # Expected output: 30
print(perimeter_pentagon(8))  # Expected output: 40
print(perimeter_pentagon(10))  # Expected output: 50
print(perimeter_pentagon(12))  # Expected output: 60
print(perimeter_pentagon(14))  # Expected output: 70

# Test with incorrect number of sides
try:
    print(perimeter_pentagon(1))  # Expected output: AssertionError
except AssertionError:
    print("Invalid number of sides")

# Test with zero sides
try:
    print(perimeter_pentagon(0))  # Expected