```
def change_base(x: int, base: int):
    convert_string = "0123456789ABCDEF"
    if x < base:
        return convert_string[x]
    else:
        return change_base(x // base, base) + convert_string[x % base]
```


Note: The code provided is a recursive function that converts an integer `x` to a base `base`. It uses the `convert_string` variable to map the numbers from 0 to 15 to their corresponding hexadecimal characters. The function works by recursively dividing the input number by the base and appending the remainder to the result string. The recursion stops when the input number is less than the base. The result string is then returned. The provided unit tests demonstrate the correct functioning of the function.