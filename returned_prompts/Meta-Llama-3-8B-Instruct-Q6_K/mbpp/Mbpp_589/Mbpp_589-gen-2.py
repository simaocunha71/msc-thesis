```
def perfect_squares(start, end):
    return [i ** 2 for i in range(int(start ** 0.5), int(end ** 0.5) + 1)]
```
The function perfect_squares takes two parameters, start and end, and returns a list of perfect squares between start and end. It uses a list comprehension to generate the list. The range function is used to generate the numbers from the square root of start to the square root of end. The square root of a number is found by raising the number to the power of 0.5. The int function is used to convert the result to an integer, as the square root of a number is not always an integer. The result is then squared to get the perfect squares. 

The unit test provided is:
assert perfect_squares(1,30)==[1, 4, 9, 16, 25] which ensures that the function works correctly. It checks that the function returns the correct list of perfect squares between 1 and 30. 

The time complexity of this function is O(n), where n is the difference between end and start. This is because the function generates a list of size n. The space complexity is also O(n), as the function returns a list of size n. 