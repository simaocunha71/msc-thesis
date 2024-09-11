Here's a Python solution using list comprehension:

```python
def cube_nums(nums):
    return [num ** 3 for num in nums]
```

Here's how it works:

- The function `cube_nums` takes in a list `nums` as an argument.
- It uses list comprehension to create a new list where each element is the cube of the corresponding element in the input list. The expression `num ** 3` cubes each number in the list.
- The resulting list is returned as the output of the function.

You can test this function using the provided assertion:

```python
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

This assertion checks if the function `cube_nums` correctly cubes the numbers in the input list and returns the expected output.

```python
def cube_nums(nums):
    return [num ** 3 for num in nums]
```

Here's an example usage of the `cube_nums` function:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = cube_nums(numbers)
print(cubes)  # Output: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

In this example, the `cube_nums` function is called with the `numbers` list as an argument. The resulting cubes of each number in the list are stored in the `cubes` variable. Finally, the `cubes` list is printed, showing the expected output.

```python
def cube_