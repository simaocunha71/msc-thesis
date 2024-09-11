Here is a Python function that counts the number of set bits in a given number:

```python
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

In this function, `n & 1` checks if the least significant bit (LSB) in the binary representation of the number is 1. If the LSB is 1, `n & 1` is 1 and `count += 1`. Then `n >>= 1` shifts `n` one bit to the right, effectively discarding the LSB. The function repeats this process until `n` becomes 0.

For example, when `n` is 2, the binary representation is `10`. The LSB is 0, so the function moves to the next bit, which is 1. The function increments `count` by 1 and shifts `n` one bit to the right. The function repeats this process until `n` becomes 0, and `count` becomes 1.

The time complexity of this function is O(log n) because it performs log(n) shifts.

Here is a test to verify that the function works correctly:

```python
print(count_Set_Bits(2) == 1)  # This should print: True
```

You can also test it with other numbers:

```python
print(count_Set_Bits(3) == 2)  # This should print: True
print(count_Set_Bits(10) == 2)  # This should print: True
print(count_Set_Bits(11) == 3)  # This should print: True
print(count_Set_Bits(0) == 0)  # This should print: True
```

These tests should all print `True`, confirming that the function is working correctly.

```python
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

This function counts the number of set bits in a given number by repeatedly checking the least significant bit (LS