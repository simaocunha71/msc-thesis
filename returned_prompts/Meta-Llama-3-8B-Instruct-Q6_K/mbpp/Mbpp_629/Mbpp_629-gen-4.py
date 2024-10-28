```
def Split(lst):
    even_nums = [num for num in lst if num % 2 == 0]
    return even_nums
```


Explanation: 
This function uses list comprehension to create a new list that includes only the even numbers from the original list. The condition `num % 2 == 0` checks if a number is even, and if it is, it is included in the new list. The function then returns this new list.

The unit test `assert Split([1,2,3,4,5]) == [2,4]` ensures that the function works correctly by checking that the function returns the expected output for a given input. 

This function can be used to find even numbers from any list of numbers. For example, `Split([1,2,3,4,5])` would return `[2,4]`, and `Split([10,20,30,40])` would return `[10,20,30,40]`. 

This function is case-insensitive, meaning it will work correctly regardless of whether the input list contains integers, floats, or a mix of both. 

This function also does not modify the original list, it creates a new list with the even numbers. This can be useful if you want to keep the original list unchanged while still having a list of even numbers. 

The time complexity of this function is O(n), where n is the number of elements in the input list, because it needs to iterate over the entire list to find the even numbers. The space complexity is also O(n), because it needs to store the even numbers in a new list. 