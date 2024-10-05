Here is a simple solution using Java's built-in Integer.toBinaryString method:

```java
public String decimalToBinary(int decimal) {
    return "db" + Integer.toBinaryString(decimal) + "db";
}
```

This method converts the given decimal number to a binary string. The binary string is then wrapped with "db" at both ends to match the required format. 

Please note that Integer.toBinaryString method returns a binary string representing the integer argument, as a signed number. The method does not include a leading sign for negative inputs.