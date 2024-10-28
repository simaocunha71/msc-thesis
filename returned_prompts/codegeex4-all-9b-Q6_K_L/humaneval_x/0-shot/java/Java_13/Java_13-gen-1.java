Here is the solution:

```java
public int greatestCommonDivisor(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return greatestCommonDivisor(b, a % b);
    }
}
```
This algorithm is based on the Euclidean algorithm for finding the greatest common divisor of two integers. It repeatedly replaces the larger number with the remainder of the division of the two numbers until the remainder is 0. At that point, the other number is the greatest common divisor.