```java
public int greatestCommonDivisor(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return greatestCommonDivisor(b, a % b);
    }
}
```
This code implements the Euclidean algorithm for finding the greatest common divisor (GCD) of two integers a and b. The algorithm works by repeatedly replacing a and b with b and a % b until b becomes 0. At that point, a is the GCD of the original a and b.