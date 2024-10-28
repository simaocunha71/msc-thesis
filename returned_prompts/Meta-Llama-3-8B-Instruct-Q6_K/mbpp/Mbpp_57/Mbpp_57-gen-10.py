```
def find_Max_Num(digits):
    digits.sort(reverse=True)
    return int(''.join(map(str, digits)))
```
The function `find_Max_Num` takes a list of digits as input and returns the largest number that can be formed with these digits. It sorts the digits in descending order and then joins them together to form the largest number. The `map` function is used to convert each digit to a string, and the `join` function is used to concatenate the strings together.

For example, if the input is `[1,2,3]`, the function will return `321`, which is the largest number that can be formed with these digits. The unit test `assert find_Max_Num([1,2,3]) == 321` confirms this.