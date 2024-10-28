Here is a simple Java solution using the built-in Integer.toBinaryString() function:

```java
public String decimalToBinary(int decimal) {
    return "db" + Integer.toBinaryString(decimal) + "db";
}
```

This function works by first converting the input integer to a binary string using the built-in Integer.toBinaryString() function. It then concatenates the resulting binary string with the "db" strings at the beginning and end. This produces the desired output.