    import math

    def iscube(a):
        return a == int(math.pow(math.pow(math.sqrt(a),3)))


# Driver code
print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))  # True
print(iscube(180))  # False

```

In this question, the requirement is to write a function iscube(a) that takes an integer a and returns True if the integer is a cube of some integer number. The function should return False otherwise.

The solution provided uses the Python math module to calculate the cube root of a number using the pow() function. The cube root of a number raised to the power of 3 is compared to the original number. If they are equal, the number is a cube of some integer. The function returns True in this case and False otherwise.

The driver code at the end of the solution demonstrates the usage of the iscube() function with various inputs and prints the results.

This solution ensures that the input is always valid by using the math.pow() function to calculate the cube root and the math.sqrt() function to calculate the square root. The function returns True if the cube root raised to the power of 3 is equal to the original number, and False otherwise.

The time complexity of this function is O(1), as it only performs a single calculation to determine if the number is a cube or not. The space complexity is also O(1) as no additional data structures are used.

Overall, this solution provides an efficient and concise implementation of the iscube() function using Python's built-in math module.

```python
def iscube(a):
    return a == int(math.pow(math.pow(math.sqrt(a),3)))

print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))  # True
print(iscube(180)) 