```
def smallest_num(lst):
    return min(lst)
```


This function uses the built-in Python function min() to find the smallest number in the list. The min() function returns the smallest item in an iterable or the smallest of two or more arguments. It's a very efficient solution, especially for large lists. 

The provided unit test `assert smallest_num([10, 20, 1, 45, 99]) == 1` ensures that the function works correctly. If the function returns 10 instead of 1, the unit test will fail. 

You can run this function with different lists to test its correctness. For example, `smallest_num([5, 2, 8, 3, 1])` should return 1. If it doesn't, there might be a bug in the function. 

The time complexity of this function is O(n), where n is the number of elements in the list, because it needs to iterate over all elements to find the smallest one. The space complexity is O(1), because it only uses a constant amount of space to store the result. 