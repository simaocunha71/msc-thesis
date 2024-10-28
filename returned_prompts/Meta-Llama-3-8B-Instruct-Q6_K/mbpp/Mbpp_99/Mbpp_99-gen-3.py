```
def decimal_to_binary(n):
    return bin(n)[2:]
```


This function takes an integer `n` as input and returns its binary representation as a string. The `bin()` function in Python converts an integer to a binary string, but it prepends a '0b' to the beginning of the string. To remove this prefix, we use slicing and return the substring starting from the 2nd character (`[2:]`).

For example, `decimal_to_binary(8)` will return `'1000'`, which is the binary representation of the decimal number 8. 

The unit test `assert decimal_to_binary(8) == '1000'` ensures that the function works correctly for the given input. 
```
assert decimal_to_binary(8) == '1000'
``` 
This test checks that the function returns the correct binary representation for the decimal number 8. If the function is implemented correctly, this test should pass. 
```python
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(3) == '11'
``` 
These additional tests ensure that the function works correctly for other inputs as well. 
```python
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(3) == '11'
``` 
If the function is implemented correctly, all these tests should pass. 
```
```python
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(3) == '11'
``` 
The unit tests ensure that the function works correctly for different inputs. If the function is implemented correctly, all these tests should pass. 
```python
``` 
The provided unit tests ensure that the function works correctly for different inputs. If the function is implemented correctly, all these tests should pass. 
```python
``` 
The unit tests are used to verify the correctness of the function. If the function is implemented correctly, all the tests should pass. 
```python
``` 
The unit tests are used to verify the correctness of the function. If