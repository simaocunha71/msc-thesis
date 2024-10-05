```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
     */
    public double poly(List<Double> xs, double x) {
        double result = 0;
        for (int i = 0; i < xs.size(); i++) {
            result += xs.get(i) * Math.pow(x, i);
        }
        return result;
    }
    
    /**
    xs are coefficients of a polynomial.
    findZero find x such that poly(x) = 0.
    findZero returns only only zero point, even if there are many.
    Moreover, findZero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> findZero(Arrays.asList(1, 2)) // f(x) = 1 + 2x
    -0.5
    >>> findZero(Arrays.asList(-6, 11, -6, 1)) // (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
     */
    public double findZero(List<Double> xs) {
        double a = xs.get(0);
        double b = xs.get(1);
        double c = xs.get(2);
        double d = xs.get(3);
        double x = 0;
        double result = 0;
        while (Math.abs(result) > 0.0001) {
            result = a + b * x + c * Math.pow(x, 2) + d * Math.pow(x, 3);
            x = x - result / (b + 2 * c * x + 3 * d * Math.pow(x, 2));
        }
        return x;
    }
}
```
This solution is based on Newton's method, which is a root-finding method that uses the derivative of a function to find its roots. In this case, the function is the polynomial `poly(xs, x)`, and the derivative is `b + 2 * c * x + 3 * d * Math.pow(x, 2)`. The method iteratively updates the value of `x` until the result