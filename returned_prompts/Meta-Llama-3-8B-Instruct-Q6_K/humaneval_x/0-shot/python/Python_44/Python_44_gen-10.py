```
def change_base(x: int, base: int):
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return ''.join(str(digit) for digit in reversed(digits))
```


Explanation:
The function `change_base` takes two parameters: `x`, the number to be converted, and `base`, the target base. The function first checks if `x` is equal to 0. If it is, the function returns the string '0'. Otherwise, it enters a loop that continues until `x` is 0. In each iteration of the loop, the function calculates the remainder of `x` divided by `base` and appends it to the list `digits`. Then, it performs integer division of `x` by `base` and updates `x`. The loop ends when `x` becomes 0. After the loop, the function joins the elements of `digits` into a string, in reverse order, and returns the result. This way, the function converts the number `x` to the target base and returns the string representation of the result. The base numbers are less than 10, so the conversion is straightforward. The function works for any base between 2 and 9. For bases greater than 9, the function would need to use a more complex approach, such as using hexadecimal digits for bases 10-16. 