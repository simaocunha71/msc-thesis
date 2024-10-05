You can simplify the given fraction by finding the greatest common divisor (GCD) of the numerator and denominator of the fraction x. Then, you can divide both the numerator and denominator of x by the GCD. If the denominator becomes 1, then the product x * n will be a whole number. Otherwise, it will not be a whole number.

Here is the implementation of the function `simplify` in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        String[] xParts = x.split("/");
        String[] nParts = n.split("/");
        
        int xNumerator = Integer.parseInt(xParts[0]);
        int xDenominator = Integer.parseInt(xParts[1]);
        int nNumerator = Integer.parseInt(nParts[0]);
        int nDenominator = Integer.parseInt(nParts[1]);
        
        int gcd = findGCD(xNumerator, xDenominator);
        xNumerator /= gcd;
        xDenominator /= gcd;
        
        int productNumerator = xNumerator * nNumerator;
        int productDenominator = xDenominator * nDenominator;
        
        return productDenominator == 1;
    }
    
    private int findGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return findGCD(b, a % b);
    }
}
```

In this code, we first split the strings x and n into their numerator and denominator parts. Then, we parse these parts into integers. We find the GCD of the numerator and denominator of x using the `findGCD` method. We divide both the numerator and denominator of x by the GCD. Then, we calculate the product of the numerators and the product of the denominators. If the product of the denominators is 1, we return true, otherwise we return false.