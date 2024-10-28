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
        if (xs.size() % 2 != 0) {
            throw new RuntimeException("xs must have even number of coefficients");
        }
        double x = xs.get(xs.size() - 1);
        double h = 1e-6;
        double result = poly(xs, x);
        while (Math.abs(result) > 1e-9) {
            double new_x = x - result / poly(xs, x + h);
            if (Math.abs(new_x - x) < 1e-9) {
                break;
            }
            x = new_x;
            result = poly(xs, x);
        }
        return x;
    }
}
```
The `findZero` method uses Newton's method for finding the root of a polynomial. It starts with an initial guess for the root (`x`) and then iteratively updates the guess until the polynomial value at the current guess is close enough to zero. The update formula is `x_new = x - f(x) / f'(x + h)`, where `f(x)`