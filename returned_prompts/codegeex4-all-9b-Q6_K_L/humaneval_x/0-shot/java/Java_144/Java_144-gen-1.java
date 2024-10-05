The problem requires to check if the product of two fractions results in a whole number. Two fractions are considered equal if their numerators and denominators are equal. 

However, the problem can be solved directly by multiplying the numerators and the denominators of the two fractions and checking if the result is a whole number. 

Here is the Java code to solve this problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean simplify(String x, String n) {
        String[] xFractions = x.split("/");
        String[] nFractions = n.split("/");
        
        int numeratorProduct = Integer.parseInt(xFractions[0]) * Integer.parseInt(nFractions[0]);
        int denominatorProduct = Integer.parseInt(xFractions[1]) * Integer.parseInt(nFractions[1]);
        
        return numeratorProduct % denominatorProduct == 0;
    }
}
```

In this code, the function `simplify` splits the input strings `x` and `n` into numerator and denominator using the `split` method. Then, it multiplies the numerators and the denominators and checks if the result is a whole number by checking if the remainder of the division is zero.