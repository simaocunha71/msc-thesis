```
def find_Max_Num(digits):
    digits.sort(reverse=True)
    return int(''.join(map(str, digits)))
```


Explanation:
The problem asks to find the largest number that can be formed using the given list of digits. This can be achieved by sorting the digits in descending order and then combining them into a single string. The `sort` function is used to sort the list in descending order, and the `join` function is used to combine the digits into a single string. The `map` function is used to convert each digit from an integer to a string before joining them. The `int` function is used to convert the resulting string back to an integer. 

For example, if the input is `[1,2,3]`, the function will return `321`, which is the largest number that can be formed using these digits. The unit test `assert find_Max_Num([1,2,3]) == 321` ensures that the function works correctly for this input. 





