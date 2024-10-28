```
def find_Max_Num(digits):
    digits.sort(reverse=True)
    return int("".join(map(str, digits)))
```
The function takes a list of digits as input, sorts them in descending order and then joins them together to form the largest possible number. The `map(str, digits)` is used to convert the digits to strings, and `int("".join(...))` is used to convert the string back to an integer.

For example, if the input is `[1,2,3]`, the function will return `321`, which is the largest possible number that can be formed with these digits. 

The unit test `assert find_Max_Num([1,2,3]) == 321` ensures that the function works correctly for this specific case. 

This function assumes that the input list contains distinct digits, and that the digits are non-negative integers. If the input list can contain duplicate digits or negative integers, the function would need to be modified accordingly. 