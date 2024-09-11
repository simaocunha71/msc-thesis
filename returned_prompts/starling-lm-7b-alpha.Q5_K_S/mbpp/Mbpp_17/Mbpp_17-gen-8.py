```
def square_perimeter(side_length):
    return 4 * side_length
```

Explanation:
The perimeter of a square is the sum of the lengths of all four of its sides. In a square, all four sides have the same length, so the perimeter is just four times the side length. The function `square_perimeter(side_length)` takes the length of one side of the square as input, and returns the perimeter of the square, which is four times that side length.

For example, if the side length is 10, then the perimeter is 40 (since 4 times 10 is 40). Therefore, the function `square_perimeter(10)` will return 40, as expected.

To test the function, you can use the `assert` statement to check if the function returns the correct result for a given input. In this case, `assert square_perimeter(10)==40` will check if the function correctly calculates the perimeter of a square with side length 10 as 40. If the assertion is true, the program will continue running; if it is false, an error will be raised.

Overall, the provided solution is a simple and straightforward function that calculates the perimeter of a square based on its side length, and correctly handles the given test case.

In Python, the `assert` statement is used to check if a condition is true. If the condition is false, an `AssertionError` is raised. The `assert` statement is often used in testing to catch errors early in the development process, and to ensure that certain conditions are met.

In this case, the `assert` statement is used to verify that the `square_perimeter` function correctly calculates the perimeter of a square with a given side length. The `assert` statement checks if the result of the function call `square_perimeter(10)` is equal to 40. If the result is not equal to 40, an error will be raised, indicating that the function is not working correctly. However, if the result is equal to 40, the `assert` statement will not raise an error, and the program will continue running normally.

By using the `assert` statement in this way, you can