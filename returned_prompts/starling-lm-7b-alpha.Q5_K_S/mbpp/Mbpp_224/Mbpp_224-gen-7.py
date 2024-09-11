Here's a Python function that counts the number of set bits in a given number:

```python
def count_Set_Bits(n):
    count = 0
    while(n > 0):
        if(n & 1):
            count += 1
        n >>= 1
    return count
```

In the function, `n` is the given number. We initialize a variable `count` to store the count of set bits. We enter a while loop that continues until `n` becomes 0. Inside the loop, we use the bitwise AND operator `&` to check if the least significant bit of `n` is 1. If it is, we increment the `count` by 1. Then, we right-shift `n` by 1 to move on to the next bit. Finally, we return the count of set bits.

You can test the function by calling `count_Set_Bits(2)` and asserting that it returns 1.

```python
assert count_Set_Bits(2) == 1
```

This assertion will pass if the function correctly counts the number of set bits in the given number.

```python
def count_Set_Bits(n):
    count = 0
    while(n > 0):
        if(n & 1):
            count += 1
        n >>= 1
    return count
```

This function works by repeatedly shifting the input value `n` to the right by one bit and checking if the least significant bit is 1. If it is, the `count` variable is incremented. This process continues until `n` becomes 0, meaning all bits have been checked. Finally, the function returns the count of set bits.

The time complexity of this function is O(log n) because the number of iterations is determined by the number of bits in the input value `n`. The space complexity is O(1) as the function only uses a single integer variable to store the count of set bits.

You can test the function by calling `count_Set_Bits(2)` and asserting that it returns 1.

```python
assert count_Set_Bits(2) == 1
```

This assertion will pass