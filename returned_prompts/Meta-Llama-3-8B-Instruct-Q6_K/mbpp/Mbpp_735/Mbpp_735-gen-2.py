```
def toggle_middle_bits(n):
    if n < 1 or n > 31:
        return "Invalid input"
    binary = bin(n)[2:]
    middle_bits = binary[1:-1]
    toggled_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    return int('1' + toggled_bits + '1', 2)
```


Explanation:
The function `toggle_middle_bits` takes an integer `n` as input, converts it to binary, and then toggles the bits in the middle part (excluding the first and last bit). The result is then converted back to an integer.

The unit test `assert toggle_middle_bits(9) == 15` is used to ensure the function works correctly. It checks that the function `toggle_middle_bits` returns `15` when given the input `9`, which is the expected output. 

This function works by first checking if the input is within the valid range of 1 to 31. If not, it returns an error message. Then, it converts the input to binary and removes the first and last bit. It then toggles the remaining bits (the middle bits) by replacing each '0' with '1' and each '1' with '0'. Finally, it adds the first and last bit back and converts the result back to an integer. 

The function also handles invalid inputs by returning an error message. This is done to ensure the function does not crash or produce incorrect results when given invalid inputs. 







Python Solution:

```python
def toggle_middle_bits(n):
    if n < 1 or n > 31:
        return "Invalid input"
    binary = bin(n)[2:]
    middle_bits = binary[1:-1]
    toggled_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
    return int('1' + toggled_bits + '1', 2)
```



This function takes an integer `n` as input, converts it to binary, and then toggles the bits in the middle part (excluding the first and last bit). The result is then converted back to an integer.

The function works by first checking if the input is within the valid range of 1 to 31. If not, it returns an error message. Then, it converts the input to binary and removes the first and last bit. It then toggles the remaining bits