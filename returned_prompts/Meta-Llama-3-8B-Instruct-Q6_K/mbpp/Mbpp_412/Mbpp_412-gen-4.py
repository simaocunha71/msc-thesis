```
def remove_odd(lst):
    return [i for i in lst if i % 2 == 0]
```
This function uses a list comprehension to create a new list that only includes the numbers from the original list that are even (i.e., have a remainder of 0 when divided by 2). The result is a new list that contains only the even numbers from the original list. 

The unit test `assert remove_odd([1,2,3]) == [2]` ensures that the function correctly removes odd numbers from the list. It checks that the output of the function when given the input `[1,2,3]` is the list `[2]`. 

For example, if you call `remove_odd([1,2,3])`, the function will return `[2]`, which is the expected output. If you call `remove_odd([4,5,6])`, the function will return `[4,6]`, which is also the expected output. 

Note that this function does not modify the original list, but instead returns a new list with the odd numbers removed. If you want to modify the original list, you can use a for loop to iterate over the list and remove the odd numbers. However, this would require more code and would not be as concise as the list comprehension used in this function. 

Here is an example of how you could modify the original list using a for loop:

```
def remove_odd(lst):
    for i in lst[:]:
        if i % 2 != 0:
            lst.remove(i)
    return lst
``` 

This function modifies the original list by removing the odd numbers. However, it is less efficient and less readable than the original function, which returns a new list with the odd numbers removed. 

In general, it is a good idea to avoid modifying the original list, especially when working with large datasets. Instead, it is often better to create a new list with the desired elements and return that list. This approach is more efficient and more readable, and it avoids the risk of accidentally modifying the original list. 