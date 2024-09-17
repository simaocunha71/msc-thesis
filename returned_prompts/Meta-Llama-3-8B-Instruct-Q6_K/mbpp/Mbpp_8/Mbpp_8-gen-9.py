```
def square_nums(nums):
    return [num ** 2 for num in nums]
```





Python code that defines a function `square_nums` which takes a list of numbers as input and returns a new list containing the squares of each number in the input list. The function uses a list comprehension to achieve this.

The unit test `assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` ensures that the function works correctly by comparing the output of the function with the expected output for a specific input.

The function `square_nums` can be used as follows:
```
print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```





The complexity of this function is O(n), where n is the number of elements in the input list, because it iterates over each element in the list once. The space complexity is also O(n), because it creates a new list containing the squares of each element in the input list.