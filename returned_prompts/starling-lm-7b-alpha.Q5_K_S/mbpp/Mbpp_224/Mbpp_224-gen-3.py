Here's a Python function that counts the number of set bits in a given number:

```python
def count_Set_Bits(n):
    count = 0
    while(n):
        n = n & (n-1)
        count += 1
    return count
```

This function works by repeatedly applying the bitwise AND operation between the number and the bitwise complement of the number. The bitwise AND operation clears the least significant set bit in the number, and the bitwise complement of the number flips all the bits. This process continues until all the bits in the number are cleared, at which point the function returns the count of the set bits.

For example, if we call `count_Set_Bits(2)`, the function will count the number of set bits in the binary representation of `2`, which is `10`. The function will then return `1`, as there is only one set bit.

Here's a test to verify the correctness of the function:

```python
def test_count_Set_Bits():
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(3) == 2
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(5) == 2
    assert count_Set_Bits(6) == 2
    assert count_Set_Bits(7) == 3
    assert count_Set_Bits(8) == 0

test_count_Set_Bits()
```

This test will pass if the function correctly counts the number of set bits in the given numbers.

```python
def count_Set_Bits(n):
    count = 0
    while(n):
        n = n & (n-1)
        count += 1
    return count
```

```python
def test_count_Set_Bits():
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(3) == 2
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(5) == 2
    assert count_Set_Bits(6) == 2
    assert count_Set