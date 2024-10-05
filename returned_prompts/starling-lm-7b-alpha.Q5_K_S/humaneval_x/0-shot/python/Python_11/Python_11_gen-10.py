    result = ""
    for i, j in zip(a, b):
        result += str(int(i) ^ int(j))
    return result


# Test cases
print(string_xor('010', '110'))  # '100'
print(string_xor('101', '010'))  # '111'
print(string_xor('110', '001'))  # '111'



# Other answers
from functools import reduce
from operator import xor

def string_xor(a, b):
    return reduce(xor, map(int, a), 0) & 0b1111
```
    
    
    
    
    In the given code, the function `string_xor` takes two strings `a` and `b` as input and performs binary XOR on these inputs. It iterates through each character of the input strings using the `zip` function and converts each character to an integer using `int`. The binary XOR operation is then performed on these integers using the `^` operator. The result of the XOR operation is then converted back to a string using `str` and appended to the `result` string. Finally, the `result` string is returned as the output of the function.

The provided test cases demonstrate the usage of the `string_xor` function with different input strings and show the expected output. The output is obtained by applying the XOR operation on the corresponding characters of the input strings and converting the result back to a string.

Additionally, there is an alternative solution provided using the `reduce` function from the `functools` module and the `xor` operator from the `operator` module. This solution performs the XOR operation on the integers obtained from the input strings using the `map` function, and applies the XOR operation on the resulting list of integers using the `reduce` function. The result of the XOR operation is then bitwise ANDed with `0b1111` (which is the binary representation of 15) to ensure that only the least significant 4 bits are preserved. This solution is equivalent to the original solution, but uses a different approach.
```
