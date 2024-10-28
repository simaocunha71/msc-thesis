```java
public String decimalToBinary(int decimal) {
    return "db" + Integer.toBinaryString(decimal) + "db";
}
```

The solution is quite straightforward. We use the `Integer.toBinaryString()` method in Java, which converts an integer to a binary string. We then add the extra characters 'db' at the beginning and the end of the string as required. The `+` operator is used to concatenate the strings. The function returns the resulting string. 

For example, if we call `decimalToBinary(15)`, it will return "db1111db", because `Integer.toBinaryString(15)` returns "1111", which is the binary representation of 15. Similarly, `decimalToBinary(32)` will return "db100000db", because `Integer.toBinaryString(32)` returns "100000", which is the binary representation of 32. 

The function is very efficient, as it only requires a single operation to convert the decimal number to binary, and then a few more operations to add the extra characters. The time complexity is O(1), which means the function runs in constant time. The space complexity is also O(1), because the function uses a fixed amount of space to store the result, regardless of the input size. 





