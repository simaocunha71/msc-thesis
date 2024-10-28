```java
public double truncateNumber(double number) {
    if (number < 0) {
        throw new IllegalArgumentException("Input must be a positive floating point number");
    }
    return number - (int)number;
}
```
This solution first checks if the input number is negative. If it is, it throws an `IllegalArgumentException` with an appropriate error message. Otherwise, it subtracts the integer part of the number from the number itself to get the decimal part and returns it.