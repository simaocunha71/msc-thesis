```
def find_Max_Num(digits):
    return int(''.join(map(str, sorted(digits, reverse=True))))
```
Explanation:
The problem is asking to find the largest number that can be formed using the given list of digits. This can be achieved by sorting the digits in descending order and then joining them together to form the largest number.

The unit test `assert find_Max_Num([1,2,3]) == 321` ensures that the function works correctly for the given input.

The `sorted` function is used to sort the digits in descending order, and the `map` function is used to convert the digits to strings so that they can be joined together. The `join` function is used to concatenate the strings together. Finally, the `int` function is used to convert the resulting string back to an integer.