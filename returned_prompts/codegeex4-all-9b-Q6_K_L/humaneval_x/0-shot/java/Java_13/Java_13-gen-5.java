```java
import java.util.*;
import java.lang.*;

class Solution {
    public int greatestCommonDivisor(int a, int b) {
        if (a == 0) {
            return b;
        }
        if (b == 0) {
            return a;
        }
        if (a == b) {
            return a;
        }
        if (a > b) {
            return greatestCommonDivisor(a - b, b);
        } else {
            return greatestCommonDivisor(a, b - a);
        }
    }
}
```
The greatest common divisor (GCD) of two integers a and b is the largest integer that divides both a and b without leaving a remainder.

The Euclidean algorithm is a well-known method for finding the GCD of two integers. It is based on the principle that the GCD of two numbers also divides their difference.

In the given code, the `greatestCommonDivisor` method implements the Euclidean algorithm. It uses recursion to repeatedly subtract the smaller number from the larger number until the two numbers are equal. At this point, the GCD is the smaller number.

The base cases for the recursion are when either a or b is 0, in which case the GCD is the non-zero number, and when a is equal to b, in which case the GCD is either a or b.

The code also handles the case where a is greater than b by recursively calling `greatestCommonDivisor` with a - b and b as the arguments. This ensures that the smaller number is always passed as the first argument to the recursive call.