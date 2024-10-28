Here is a solution in Java:

```java
public String decimalToBinary(int decimal) {
    String binary = Integer.toBinaryString(decimal);
    return "db" + binary + "db";
}
```

This solution uses the built-in `Integer.toBinaryString()` function to convert the decimal number to a binary string. The `Integer.toBinaryString()` function returns a binary string that represents the value of the specified integer. Then, it prepends and appends "db" to the binary string, and returns the result.