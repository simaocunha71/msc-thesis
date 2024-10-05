```java
public double truncateNumber(double number) {
    int intPart = (int) number;
    return number - intPart;
}
```
Explanation:
We use the fact that the integer part of a number is the largest integer smaller than the number. We cast the number to an integer using `(int) number`, which effectively truncates the decimal part and returns the integer part.

Then, we subtract the integer part from the original number to get the decimal part. This decimal part is the remainder of the division of the original number by 1, which is the definition of the decimal part.

For example, for the input 3.5, the integer part is 3, and subtracting 3 from 3.5 gives 0.5, which is the decimal part.

This solution has a time complexity of O(1), as it only involves a single cast and subtraction operation. It is also accurate and efficient, as it does not involve any floating-point arithmetic operations that could introduce precision errors.