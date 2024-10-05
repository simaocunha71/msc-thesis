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
        double y = 0;
        double z = 0;
        double w = 0;
        double e = 0;
        double f = 0;
        double g = 0;
        double h = 0;
        double i = 0;
        double j = 0;
        double k = 0;
        double l = 0;
        double m = 0;
        double n = 0;
        double o = 0;
        double p = 0;
        double q = 0;
        double r = 0;
        double s = 0;
        double t = 0;
        double u = 0;
        double v = 0;
        double w = 0;
        double x = 0;
        double y = 0;
        double z = 0;
