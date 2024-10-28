Here is the solution:

```java
import java.util.*;

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
        if (xs.size() % 2 == 1) {
            throw new RuntimeException("List xs must have even number of coefficients");
        }
        double x = xs.get(xs.size() - 1); // start from the last coefficient
        double tolerance = 1e-9; // precision
        double dx = 1e-7; // step size
        double prevResult = Double.MAX_VALUE;
        while (true) {
            double result = poly(xs, x);
            if (Math.abs(result) < tolerance) {
                return x;
            }
            if (Math.abs(result - prevResult) < tolerance) {
                // if the result is not changing, we can stop
                return x;
            }
            prevResult = result;
            x -= result / poly(new ArrayList<>(Arrays.asList(1, 1)), x); // update x using Newton's method
        }
    }
}
```

In this solution, the `findZero` method uses Newton's method to find the root of the polynomial. It starts from the