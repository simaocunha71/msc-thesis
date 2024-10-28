```
def change_base(x: int, base: int):
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x//base, base) + convertString[x%base]
```


The function `change_base` converts an integer `x` to a different base `base`. The base conversion is done recursively by repeatedly dividing `x` by `base` and appending the remainder to the result. The remainder is used as an index to the `convertString` which contains the digits of the new base. The function returns a string representation of the converted number. The base numbers are less than 10 and the base conversion is done in the range [2, 10]. The function is tested with examples in the problem statement. The time complexity of this function is O(log(x)) because the division operation is performed in each recursive call, and the space complexity is O(log(x)) because the maximum depth of the recursion is log(x). 