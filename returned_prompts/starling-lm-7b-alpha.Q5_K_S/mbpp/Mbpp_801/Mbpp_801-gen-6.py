def test_three_equal(num1, num2, num3):
    counter = 0
    if num1 == num2:
        counter += 1
    if num2 == num3:
        counter += 1
    if num1 == num3:
        counter += 1
    return counter

# Calling the function
print(test_three_equal(1, 1, 1))  # Should print 3

# Testing for different inputs
print(test_three_equal(1, 2, 2))  # Should print 2
print(test_three_equal(2, 2, 3))  # Should print 1
print(test_three_equal(3, 3, 3))  # Should print 3
print(test_three_equal(1, 2, 3))  # Should print 0

"""
A python function has been defined as test_three_equal that takes in three integers as arguments (num1, num2, num3). The function counts the number of times these three numbers appear equal to each other and returns this count. The function is tested with several example inputs and the results are printed.
"""

```python
# Python Function to Count Equal Integers
def test_three_equal(num1, num2, num3):
    counter = 0
    if num1 == num2:
        counter += 1
    if num2 == num3:
        counter += 1
    if num1 == num3:
        counter += 1
    return counter

# Testing the function with different inputs
print(test_three_equal(1, 1, 1))  # Should print 3
print(test_three_equal(1, 2, 2))  # Should print 2
print(test_three_equal(2, 2, 3))  # Should print 1
print(test_three_equal(3, 3, 3))  # Should print 3
print(test_three_equal(1, 2, 3))  # Should print 0
```

In the provided Python code, a function named `test_three_equal` is defined. This function takes three