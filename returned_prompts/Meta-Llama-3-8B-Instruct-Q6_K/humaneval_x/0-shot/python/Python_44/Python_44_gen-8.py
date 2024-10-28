```
def change_base(x: int, base: int):
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x//base, base) + convertString[x%base]
```
This function works by recursively dividing the input number `x` by the base, and appending the remainder to the result. The remainder is used as an index to the `convertString` which contains the characters to use for each digit in the new base. The base case for the recursion is when `x` is less than the base, in which case we simply return the character at index `x` in `convertString`. The recursive case is when `x` is greater than or equal to the base, in which case we recursively call `change_base` with `x//base` (integer division) and append the character at index `x%base` (the remainder) to the result. The function returns a string representation of the number in the new base. 

For example, `change_base(8, 3)` returns `'22'` because 8 in base 10 is 22 in base 3. `change_base(8, 2)` returns `'1000'` because 8 in base 10 is 1000 in base 2. `change_base(7, 2)` returns `'111'` because 7 in base 10 is 111 in base 2. 

Note: This function assumes that the input base is less than 10, as specified in the problem statement. If the input base can be greater than 10, additional logic would be needed to handle the case where `x` is greater than or equal to the base. 

Also, this function does not handle the case where `x` is negative. If negative numbers are to be supported, the function would need to be modified to handle this case. 

Finally, the function does not handle the case where `base` is less than 2. If bases less than 2 are to be supported, the function would need to be modified to handle this case.  In this case, the function would need to return an error message or raise an exception, as there is no way to represent a number in a base less than 2. 