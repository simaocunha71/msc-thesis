```
def perfect_squares(start, end):
    return [i for i in range(start, end+1) if int(i**0.5)**2 == i]
```



The problem is asking you to write a function that takes two numbers as input and returns a list of perfect squares between those two numbers. For example, if the input is (1,30), the output should be [1,4,9,16,25].

The unit test `assert perfect_squares(1,30)==[1, 4, 9, 16, 25]` helps to clarify the problem by providing an example of the expected output.

Here's the solution in Python:
```
def perfect_squares(start, end):
    return [i for i in range(start, end+1) if int(i**0.5)**2 == i]
```
This function uses a list comprehension to iterate over the range of numbers from `start` to `end` (inclusive), and includes a number in the output list if it is a perfect square. A number is considered a perfect square if the square root of the number is an integer. The `int(i**0.5)**2` expression calculates the square root of `i` and checks if it is an integer by squaring it and comparing it to `i`. If they are equal, then `i` is a perfect square. The `range` function is used to generate the numbers from `start` to `end`, and the `+1` is used to include `end` in the range. The list comprehension is used to filter the numbers and only include the perfect squares in the output list.