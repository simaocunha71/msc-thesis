def toggle_middle_bits(n):
    """
    Toggle bits of the number except the first and the last bit.
    """
    # Create a copy of the number
    num = n

    # Toggle all bits except the first and the last bit
    while num > 0:
        if num % 2 == 0:
            num = num >> 1
        else:
            num = num >> 1
            num = num | 1

    # Return the result
    return num

# Test the function
print(toggle_middle_bits(9))  # Should print 15
























"""
In this code, we define a function called toggle_middle_bits that takes an integer as input. Inside the function, we create a copy of the input number and assign it to the variable "num". Then, we enter a while loop that continues until the number becomes zero.

Inside the while loop, we check if the least significant bit of the number is 0. If it is, we shift the number one bit to the right using the bitwise right shift operator (>>). If the least significant bit is 1, we shift the number one bit to the right, and then perform a bitwise OR operation (|) with 1. This effectively toggles the bit.

After the while loop, we return the modified number, which now has all the bits except the first and the last bit toggled.

Finally, we test the function by calling it with the input 9 and printing the result, which should be 15.
"""



```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

