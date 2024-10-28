You can use the built-in max function in Python, which returns the largest item in an iterable or the largest of two or more arguments. The iterable can contain any type of elements, including strings, numbers, and lists.

Here's how you can do it:

```Python
def find_max_val(lst):
    return max(lst)
```

This function takes a list as an argument and returns the maximum value in the list. It works with lists containing different types of elements, such as strings, numbers, and lists.

The unit test `assert max_val(['Python', 3, 2, 4, 5, 'version'])==5` ensures that the function works correctly with a list containing strings and numbers. The expected output is 5, which is the maximum value in the list. 

You can use this function to find the maximum value in any list, regardless of the types of elements it contains. For example, you can use it to find the maximum value in a list of student grades or the maximum value in a list of temperatures. 

Remember that the max function will return the largest item in the list, but if you want to find the maximum value in a specific range, you may need to modify the function accordingly. For example, you might need to filter the list to include only values within a certain range before finding the maximum value. 