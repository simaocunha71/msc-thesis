You can use the modulus operator (%) to get the decimal part of a number. The modulus operator returns the remainder of a division.

Here is the code:

```java
public double truncateNumber(double number) {
    return number % 1;
}
```

This code works by taking the modulus of the number with 1, which will give you the decimal part of the number.