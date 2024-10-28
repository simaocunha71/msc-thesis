```
def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
    return None
```
This function iterates over the list and checks each number to see if it's odd (i.e., if the remainder when divided by 2 is not 0). If it finds an odd number, it returns that number. If it doesn't find any odd numbers, it returns `None`. 

Note that the unit test `assert first_odd([1,3,5]) == 1` suggests that the function should return the first odd number it encounters, not all the odd numbers. 

If you want to return all the odd numbers, you could modify the function to return a list of all the odd numbers it finds:
```
def first_odd(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers[0] if odd_numbers else None
``` 
This function uses a list comprehension to create a list of all the odd numbers in the input list, and then returns the first element of that list. If the list is empty (i.e., there are no odd numbers), it returns `None`.  This function would pass the unit test `assert first_odd([1,3,5]) == 1`, but it would also pass `assert first_odd([2,4,6]) == None`, even though there are no odd numbers in that list.  If you want to raise an error in that case, you could modify the function to use the `or` operator to return a default value if the list is empty:
```
def first_odd(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers[0] or None
``` 
This function would raise a `IndexError` if the list is empty, because it tries to access the first element of an empty list.  If you want to avoid that, you could use the `or` operator with a default value:
```
def first_odd(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers[0] or None
``` 
This function would return `None` if the list is empty, without raising an error.  This is probably the most robust way to handle the case where the list is empty.  It's also the most flexible, because it allows