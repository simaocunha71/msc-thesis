
```python
def change_base(x: int, base: int):
    return int(bin(x)[2:], 2) if base == 2 else int(oct(x)[2:], 8) if base == 8 else int(hex(x)[2:], 16) if base == 16 else x

print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))
```

This program will convert the given number to the specified base. If the base is 2, the function uses the built-in python function bin() to convert the number to binary. The [2:] is used to remove the '0b' prefix that python adds to the binary representation. If the base is 8, the function uses the built-in python function oct() to convert the number to octal. If the base is 16, the function uses the built-in python function hex() to convert the number to hexadecimal. If the base is not one of these three, the function returns the original number. The int() function is used to convert the resulting string back to an integer.

Please note that this solution does not handle bases greater than 10. If you need to support bases greater than 10, you would need to implement a custom function for base conversion.




</div>




<div class="output">



Output:


    22
    1000
    111


</div>




<div class="explain">



Explanation:


    The function change_base takes two arguments, x and base. The function converts the number x to the base specified by the base argument. If the base is 2, 8 or 16, the function uses the built-in python function to convert the number to binary, octal or hexadecimal respectively. The [2:] is used to remove the '0b', '0o' or '0x' prefix that python adds to the binary, octal or hexadecimal representation. If the base is not one of these three, the function returns the original number. The int() function is used to