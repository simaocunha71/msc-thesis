```
def remove_odd(lst):
    return [i for i in lst if i % 2 == 0]
```
This function uses a list comprehension to create a new list that includes only the even numbers from the original list. The condition `i % 2 == 0` is used to check if a number is even. If the number is even, it is included in the new list. The function returns the new list. 

For example, if we call `remove_odd([1,2,3])`, it will return `[2]`. 

The unit test `assert remove_odd([1,2,3]) == [2]` confirms that this function works correctly. It checks that the function returns the list `[2]` when given the input `[1,2,3]`. 

Note: The original list is not modified, a new list is created with only the even numbers. If you want to modify the original list, you can use a for loop and the `remove` method. For example: `for i in lst[:]: if i % 2 != 0: lst.remove(i)`. However, this approach is not recommended as it modifies the original list and can have unintended consequences. The list comprehension approach is generally safer and more efficient. 