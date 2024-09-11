Here's a Python function that can be used to toggle bits of the number except the first and the last bit:

```python
def toggle_middle_bits(n):
    # Convert the number to binary
    binary = bin(n)[2:]
    
    # Get the length of the binary string
    length = len(binary)
    
    # Toggle all bits except the first and the last bit
    for i in range(1, length-1):
        # Convert the bit at index i to 1 if it's 0 and vice versa
        if binary[i] == '0':
            binary = binary[:i] + '1' + binary[i+1:]
        else:
            binary = binary[:i] + '0' + binary[i+1:]
    
    # Convert the binary string back to an integer
    return int(binary, 2)
```

This function works by first converting the input number to a binary string. It then iterates over each bit in the string, starting from the second bit, and toggles it. If the bit is currently 0, it is replaced with 1, and if the bit is currently 1, it is replaced with 0. The function does not modify the first and the last bit of the string. Finally, the function converts the modified binary string back to an integer and returns the result.

You can test the function with the provided assert statement:

```python
assert toggle_middle_bits(9) == 15
```

This should return True, indicating that the function is correctly toggling the middle bits of the number.

```python
def toggle_middle_bits(n):
    # Convert the number to binary
    binary = bin(n)[2:]
    
    # Get the length of the binary string
    length = len(binary)
    
    # Toggle all bits except the first and the last bit
    for i in range(1, length-1):
        # Convert the bit at index i to 1 if it's 0 and vice versa
        if binary[i] == '0':
            binary = binary[:i] + '1' + binary[i+1:]
        else:
