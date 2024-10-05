Here is a Java solution. The idea is to calculate the least common multiple (LCM) of the denominators of the two fractions and see if the numerator of the first fraction multiplied by the LCM is a multiple of the numerator of the second fraction:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        String[] xParts = x.split("/");
        String[] nParts = n.split("/");

        int xNum = Integer.parseInt(xParts[0]);
        int xDenom = Integer.parseInt(xParts[1]);

        int nNum = Integer.parseInt(nParts[0]);
        int nDenom = Integer.parseInt(nParts[1]);

        int lcm = lcm(xDenom, nDenom);

        return (xNum * lcm) % nDenom == 0;
    }

    private int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }

    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
}
```

The `simplify` function first splits the input strings into numerator and denominator parts. Then it calculates the least common multiple (LCM) of the denominators using the `lcm` function. Finally, it checks if the numerator of the first fraction multiplied by the LCM is a multiple of the numerator of the second fraction. If it is, it returns `true`, otherwise it returns `false`.

The `lcm` function calculates the least common multiple of two integers using the formula `lcm(a, b) = a * (b / gcd(a, b))`, where `gcd` is the greatest common divisor of `a` and `b`. The `gcd` function calculates the greatest common divisor of two integers using the Euclidean algorithm.