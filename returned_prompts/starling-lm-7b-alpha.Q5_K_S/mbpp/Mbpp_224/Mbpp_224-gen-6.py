```
def count_Set_Bits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count
```

Explanation:
In this code, the function `count_Set_Bits` takes a number `n` as input and returns the count of set bits in it. 

The function uses a while loop to iterate through the binary representation of the number `n` from the right (least significant bit) to the left (most significant bit). 

Inside the loop, it checks if the least significant bit of `n` is set (i.e., has a value of 1). This is done by performing a bitwise AND operation between `n` and 1 (`n & 1`). If the result is non-zero, it means the bit is set, and the count is incremented by 1. 

Then, the function right-shifts `n` by 1 bit (`n >>= 1`) to move on to the next bit in the binary representation. This process continues until all bits have been traversed, and the count of set bits is returned.

The `assert` statement at the beginning of the code is used to verify the correctness of the function. It checks if the function correctly counts the set bits in the number 2, which should return 1. If the assertion fails, it raises an error, indicating that the function is not working as expected.

Overall, this function provides a concise and efficient way to count the number of set bits in a given number in Python.

```python
# Example usage:
print(count_Set_Bits(11))  # Output: 3 (binary representation of 11 is 1011, which has 3 set bits)
```

You can use the `count_Set_Bits` function to count the number of set bits in any positive integer by passing the number as an argument to the function.

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