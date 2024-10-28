```
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]
```
This function uses list comprehension to create two lists. The first list includes all non-zero elements from the original list, and the second list includes all zero elements from the original list. It then concatenates these two lists to return the result. This function assumes that the input list is a list of integers. If the input list is a list of other types of objects, the function may need to be modified accordingly. For example, if the input list is a list of strings, the function would need to be modified to check if a string is equal to "0" instead of checking if it is equal to 0. 

The unit test `assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]` ensures that the function works correctly for the given input. It checks if the output of the function is equal to the expected output for the given input. If the output is not equal to the expected output, the function is considered to have failed the test. 

This function has a time complexity of O(n), where n is the length of the input list. This is because it needs to iterate over the input list twice, once to create the list of non-zero elements and once to create the list of zero elements. The space complexity of this function is also O(n), as it creates two lists that can be as large as the input list. 

Here is how you can use this function:
```
print(move_zero([1,0,2,0,3,4]))  # Output: [1,2,3,4,0,0]
```  # Output: [1,2,3,4,0,0]
```
This will print the result of moving all zeroes to the end of the list [1,0,2,0,3,4]. The output will be [1,2,3,4,0,0].  # Output: [1,2,3,4,0,0]```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
