
    import math

    def sum_squares(lst):
        return sum([math.ceil(x)**2 for x in lst])


# Test cases
print(sum_squares([1, 2, 3]))  # 14
print(sum_squares([1, 4, 9]))  # 98
print(sum_squares([1, 3, 5, 7]))  # 84
print(sum_squares([1.4, 4.2, 0]))  # 29
print(sum_squares([-2.4, 1, 1]))  # 6


This problem is a bit tricky because it involves rounding up to the nearest integer before squaring each number, and summing those squares. The solution uses Python's built-in `math.ceil` function to round numbers up, and list comprehensions to square each number and sum them all up.

Here is the explanation of the code:
- We import the math module to use the ceil function.
- We define the function sum_squares that takes a list of numbers lst as its argument.
- Inside the function, we use a list comprehension to square each number in the list by raising it to the power of 2, but first we use math.ceil to round it up to the nearest integer.
- We then use the built-in sum function to add up all the squared numbers and return the result.
- Finally, we test the function with a few test cases.



# Python Program to Reverse the Words in a Sentence

