```
def remove_odd(lst):
    return [num for num in lst if num % 2 == 0]
``` 
The function `remove_odd` takes a list `lst` as an argument and returns a new list that contains only the even numbers from the original list. It does this by using a list comprehension that iterates over the original list and includes only the numbers that are divisible by 2 (i.e., the even numbers). 

The unit test `assert remove_odd([1,2,3]) == [2]` ensures that the function works correctly. It checks that when the input is `[1,2,3]`, the output is `[2]`, which is the only even number in the list. 

This function is efficient because it only iterates over the original list once, and it uses a list comprehension, which is a concise and efficient way to create a new list. 
```
print(remove_odd([1,2,3])) # Output: [2]
``` 
The output is `[2]` as expected.  It has successfully removed the odd numbers from the list.  The function works correctly for any list of numbers, not just `[1,2,3]`.  For example, `remove_odd([1,2,3,4,5,6])` would return `[2,4,6]`. 
```
print(remove_odd([1,2,3,4,5,6])) # Output: [2,4,6]
``` 
The output is `[2,4,6]` as expected.  It has successfully removed the odd numbers from the list.  The function works correctly for any list of numbers. 
```
print(remove_odd([5,6,7,8,9,10])) # Output: [6,8,10]
``` 
The output is `[6,8,10]` as expected.  It has successfully removed the odd numbers from the list.  The function works correctly for any list of numbers. 
```
print(remove_odd([1,3,5,7,9])) # Output: []
``` 
The output is `[]` as expected.  It has successfully removed all the odd numbers from the list.  The function works correctly even when there are no even numbers in the list. 
```
print(remove_odd([2,4,6,8,10])) # Output: [2,4,6,8,10]
``` 
The