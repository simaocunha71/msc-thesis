"""
def toggle_middle_bits(n):
    x = n >> 1
    x |= x << 1
    x = ~x & 0b1111
    x <<= 1
    x |= n & 0b11
    return x

def test_toggle_middle_bits():
    assert toggle_middle_bits(9) == 15

test_toggle_middle_bits()
"""

Explanation:
This function `toggle_middle_bits` takes a number `n` and toggles the middle bits of the number except the first and the last bit. Here's a step-by-step explanation of the code:

1. The variable `x` is initialized as the bitwise right shift of `n` by 1, which essentially means `x = n >> 1`. This is done to shift all the bits of `n` one position to the right.

2. The bitwise OR operation (`|`) is performed between `x` and the bitwise left shift of `x` by 1 (`x << 1`). This operation effectively sets all the even-indexed bits of `x` to 1.

3. The bitwise NOT operation (`~`) is applied to `x` to invert all its bits. Then, the bitwise AND operation (`&`) is performed between the inverted `x` and the binary representation of `1111` (0b1111), which is a binary number with all bits set to 1. This operation effectively clears all the even-indexed bits of `x` that were set to 1 in the previous step.

4. The left shift (`<<`) operation is applied to `x` by 1, which shifts all the bits of `x` one position to the left.

5. The bitwise OR operation (`|`) is performed between `x` and the bitwise AND operation (`&`) between `n` and the binary representation of `11` (0b11). This operation effectively sets the first and the last bits of `x` to the corresponding bits of `n`, while the middle bits remain unchanged.

6. The function returns the updated value of `x`, which represents the number with the middle bits toggled except