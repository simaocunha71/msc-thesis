```
def decimal_to_binary(n):
    return bin(n)[2:]
```


This function converts the given decimal number to its binary equivalent using the built-in `bin()` function in Python. The `[2:]` at the end is used to remove the '0b' prefix that `bin()` adds to the binary representation. For example, `bin(8)` returns '0b1000', but `bin(8)[2:]` returns '1000'. The function will return '1000' when called with `decimal_to_binary(8)`. 

The unit test provided ensures that the function works correctly, as `decimal_to_binary(8)` should return '1000', which is the binary equivalent of the decimal number 8. The function will pass this test. 

Please note that the unit test `assert decimal_to_binary(8) == '1000'` is used to verify the correctness of the function. This test ensures that the function returns the expected binary representation of the decimal number 8. If the function returns anything other than '1000', the test will fail. 

This function is efficient and scalable, as it uses built-in Python functions and does not require any manual bit manipulation or string concatenation. It is also easy to read and understand, making it a good choice for most use cases. 





