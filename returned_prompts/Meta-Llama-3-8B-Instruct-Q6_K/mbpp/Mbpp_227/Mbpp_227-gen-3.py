```
def min_of_three(a, b, c):
    return min(a, b, c)
```
This function takes three numbers as input and returns the smallest one. The unit test `assert min_of_three(10,20,0)==0` ensures that the function works correctly. 

In Python, the built-in `min` function can be used to find the minimum of a list of numbers. So, we can directly use `min(a, b, c)` to find the minimum of three numbers. 

Note: The `min` function returns the smallest item in an iterable or the smallest of two or more arguments. It is a built-in function in Python. 
```python
min(iterable)
min(a, b, c)
``` 
Here, `iterable` is any iterable (such as a list, tuple, or string), and `a`, `b`, and `c` are numbers. The `min` function returns the smallest item in the iterable or the smallest of `a`, `b`, and `c`. If the iterable is empty, it returns `None`. If there are multiple smallest items, it returns the first one it encounters.  If you want to get all the smallest items, you can use a list comprehension and a conditional statement. 

For example:
```
numbers = [1, 2, 3, 4, 5]
smallest = min(numbers)
print(smallest)  # Output: 1
``` 
or 
```
numbers = [1, 2, 3, 4, 5]
smallest = min((x for x in numbers if x == min(numbers)))
print(smallest)  # Output: 1
``` 
This will return all the smallest items in the list. If you want to return all the smallest items as a list, you can use a list comprehension:
```
numbers = [1, 2, 3, 4, 5]
smallest = [x for x in numbers if x == min(numbers)]
print(smallest)  # Output: [1]
``` 
Please note that the `min` function is not limited to finding the smallest number in a list. It can also be used to find the smallest of two or more numbers. For example:
```
a = 10
b = 20
c = 5
smallest = min(a, b, c)
print(smallest)  # Output: 5
``` 
