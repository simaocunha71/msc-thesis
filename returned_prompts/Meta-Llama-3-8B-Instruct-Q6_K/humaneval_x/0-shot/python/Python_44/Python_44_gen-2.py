```
def change_base(x: int, base: int):
    convertString = "0123456789ABCDEF"
    result = ""

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result
```
This function works by repeatedly dividing the input number `x` by the base and appending the remainder to the result string. The remainder is obtained by taking the modulus of `x` with the base. The division is done using integer division (`//` operator), which discards the remainder and returns the quotient. The process continues until `x` becomes 0. The result string is then returned.

For example, when `x` is 8 and `base` is 3, the function works as follows:
```
x = 8
base = 3
result = ""

while x > 0:
    result = "2" + result  # remainder 2
    x = 8 // 3  # quotient 2, remainder 2
    result = "2" + result  # remainder 2
    x = 2 // 3  # quotient 0, remainder 2
    x = 0  # loop ends

return "22"  # result
```
The function returns the string "22", which is the base-3 representation of the number 8. Similarly, when `x` is 8 and `base` is 2, the function returns the string "1000", which is the base-2 representation of the number 8. When `x` is 7 and `base` is 2, the function returns the string "111", which is the base-2 representation of the number 7.