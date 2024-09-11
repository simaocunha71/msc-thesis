"""
To toggle the bits of a number except the first and the last bit, you can use bitwise operations. Here's a step-by-step breakdown of the solution:

1. First, use the right shift operator (>>) to shift all the bits in the number one position to the right. This will effectively move all the bits to the right, except for the last bit, which will become the first bit.

2. Next, use the left shift operator (<<) to shift the last bit (which is now the first bit) one position to the left. This will effectively move the first bit to the end of the number, while the rest of the bits remain in the same positions.

3. Finally, use the bitwise XOR operator (^) to toggle all the bits in the number. The XOR operation will flip each bit to its opposite value, effectively toggling them.

Here's an example of how the function can be implemented:

def toggle_middle_bits(n):
    # Shift all bits to the right, except for the last bit
    n = (n >> 1) | (n & 1) << 1
    # Shift the last bit to the end and toggle all other bits
    return (n ^ (n >> 1))

You can verify the correctness of the function using the provided assert statement:

assert toggle_middle_bits(9) == 15

This assertion will pass if the function correctly toggles the bits of the number 9, resulting in the number 15.
"""

def toggle_middle_bits(n):
    # Shift all bits to the right, except for the last bit
    n = (n >> 1) | (n & 1) << 1
    # Shift the last bit to the end and toggle all other bits
    return (n ^ (n >> 1))

assert toggle_middle_bits(9) == 15

"""
Explanation:

To toggle the bits of a number, we can use the bitwise XOR operator (^). The XOR operation will flip each bit to its opposite value, effectively toggling them. However, we want to toggle all bits except for the first and the last bit. To achieve this, we can shift all bits to the right