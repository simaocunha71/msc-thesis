Here's a Python function that counts the number of set bits in a given number:

```python
def count_Set_Bits(n):
    count = 0
    while(n):
        n = n & (n-1)
        count += 1
    return count
```

In this function, we use a while loop to repeatedly perform bitwise AND operation (n = n & (n-1)) until n becomes 0. Each time we perform this operation, we increment the count variable. The bitwise AND operation clears the rightmost set bit in the number, so after each operation, the count of set bits is reduced by one. When the operation becomes invalid and n becomes 0, it means that we have counted all the set bits. Finally, we return the count variable, which holds the total count of set bits in the original number.

The time complexity of this function is O(log n) because the number of times the loop runs is equal to the number of set bits in the original number.

You can test the function with the provided assertion:

```python
assert count_Set_Bits(2) == 1
```

This assertion checks if the function correctly counts the number of set bits in the number 2, which should be 1.

"""

```python
def count_Set_Bits(n):
    count = 0
    while(n):
        n = n & (n-1)
        count += 1
    return count
```

```python
assert count_Set_Bits(2) == 1
```

"""

```python
def count_Set_Bits(n):
    count = 0
    while(n):
        n = n & (n-1)
        count += 1
    return count
```

```python
assert count_Set_Bits(2) == 1
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
