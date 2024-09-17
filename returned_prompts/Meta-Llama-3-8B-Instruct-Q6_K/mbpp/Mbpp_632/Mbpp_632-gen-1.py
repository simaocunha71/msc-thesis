```
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]
```
This function uses list comprehension to separate the list into two parts: one with non-zero elements and one with zero elements. It then concatenates these two lists to return the result. The unit test provided ensures that the function works correctly.

For example, when the input is [1,0,2,0,3,4], the function returns [1,2,3,4,0,0], which is the desired output. The function works for any list, not just the one provided in the unit test. It efficiently handles large lists and provides a clear and concise solution to the problem.