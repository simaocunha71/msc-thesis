```
def remove_odd(lst):
    return [x for x in lst if x % 2 == 0]
```
The function `remove_odd` takes a list `lst` as input and returns a new list containing only the even numbers from the original list. It uses a list comprehension to iterate over the input list and includes only the elements that satisfy the condition `x % 2 == 0`, which is true for even numbers. The function does not modify the original list and returns a new list with the even numbers. The unit test `assert remove_odd([1,2,3]) == [2]` ensures that the function works correctly. 

The time complexity of this function is O(n), where n is the length of the input list, because it needs to iterate over each element in the list once. The space complexity is also O(n), because it needs to store the result in a new list. 

This function can be used to remove odd numbers from a list, and it is more efficient and readable than using a loop or the `filter` function. 

For example, if you have a list `numbers = [1, 2, 3, 4, 5, 6]`, you can use this function to remove the odd numbers like this:
```
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = remove_odd(numbers)
print(even_numbers)  # Output: [2, 4, 6]
``` 
This will remove the odd numbers from the list and return a new list containing only the even numbers. The original list remains unchanged. 