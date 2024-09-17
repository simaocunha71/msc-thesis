```
def filter_oddnumbers(lst):
    return [x for x in lst if x % 2 != 0]
```
This function uses list comprehension to create a new list that includes only the odd numbers from the input list. The condition `x % 2 != 0` is used to filter out the even numbers. 

For example, when the input is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the output will be `[1,3,5,7,9]`. 

This function is tested with the unit test `assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]`. 

Note that this function does not modify the original list, it creates a new list with the filtered elements. If you want to modify the original list, you can use a for loop and append the odd numbers to the list. For example:
```
def filter_oddnumbers(lst):
    for i in lst:
        if i % 2 != 0:
            lst.remove(i)
    return lst
``` 
However, this approach is not recommended as it modifies the original list and can have unintended consequences. The list comprehension approach is generally safer and more efficient. 