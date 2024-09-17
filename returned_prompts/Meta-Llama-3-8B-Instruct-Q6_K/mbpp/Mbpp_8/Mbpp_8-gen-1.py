```
def square_nums(nums):
    return [num ** 2 for num in nums]
```


This function uses a list comprehension to create a new list where each element is the square of the corresponding element in the input list.

The unit test provided ensures that the function works correctly for the given input. The expected output is a list of squares of numbers from 1 to 10. 

For example, the square of 3 is 9, the square of 4 is 16, and so on. The function correctly calculates these squares and returns the list [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 

This function is efficient because it uses a list comprehension, which is a concise and efficient way to create a new list in Python. It also has a time complexity of O(n), where n is the length of the input list, because it only needs to iterate over the input list once. 

This function is also easy to read and understand, making it a good choice for a programming problem that requires a clear and concise solution. 

Note: The unit test provided is a good practice in programming, as it ensures that the function works correctly for a given input. This helps to catch any bugs or errors early on, making it easier to debug and maintain the code. 

Also, the function is flexible and can be used with any list of numbers, not just the specific list provided in the unit test. This makes it a reusable and versatile function that can be applied to a wide range of problems. 