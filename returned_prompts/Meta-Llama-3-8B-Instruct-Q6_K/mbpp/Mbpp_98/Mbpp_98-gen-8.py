```
def multiply_num(lst):
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)
```



The task is to write a function that takes a list of numbers as input, multiplies all the numbers together, and then divides the result by the length of the list.

The unit test `assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)` helps to clarify the expected output of the function. It suggests that the function should return a floating-point number, not an integer.

Here is a Python function that solves the problem:
```
def multiply_num(lst):
    product = 1
    for num in lst:
        product *= num
    return product / len(lst)
```
This function initializes a variable `product` to 1, then iterates over the input list `lst`. For each number in the list, it multiplies `product` by that number. Finally, it returns the result of dividing `product` by the length of the list. This is equivalent to multiplying all the numbers together and then dividing by the number of numbers.