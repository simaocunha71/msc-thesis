```
def find_Max_Num(digits):
    return int(''.join(map(str, sorted(digits, reverse=True))))
```


The function `find_Max_Num` takes a list of digits as input. It sorts the list in descending order and then joins the sorted list into a string. The `int` function is used to convert the string back into an integer. This way, the function returns the largest number that can be formed with the given list of digits. 

For example, if the input is `[1,2,3]`, the output will be `321`, which is the largest number that can be formed with these digits. 

The unit test `assert find_Max_Num([1,2,3]) == 321` ensures that the function works correctly.  It checks if the output of `find_Max_Num([1,2,3])` is `321`, which it should be. 

This function assumes that the input list contains only unique digits. If the list can contain duplicate digits, the function may not work correctly. For example, if the input is `[1,2,2]`, the function will return `222`, which is not the largest number that can be formed with these digits. To handle duplicate digits, the function would need to be modified. 

The function also assumes that the input list contains at least one digit. If the list is empty, the function will return `0`, which may not be the expected result. To handle an empty list, the function could be modified to return an error message or a special value. 