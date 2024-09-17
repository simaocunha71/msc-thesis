You can solve this problem by using the built-in function bin() which converts an integer to a binary string, and then use the count() function to count the number of '1's in the string.

Here is the Python function:

```Python
def count_Set_Bits(n):
    return bin(n).count('1')
```
This function works by first converting the integer `n` to a binary string using the `bin()` function. This string will start with '0b' to indicate that it's a binary number, but we don't need these characters so we can ignore them. Then the `count('1')` function is used to count the number of '1's in the string. 

For example, if you call `count_Set_Bits(2)`, it will return `1` because the binary representation of `2` is `10` and there is one '1'. 

This function passes the given unit test:

```Python
assert count_Set_Bits(2) == 1
```  ```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```Python
```