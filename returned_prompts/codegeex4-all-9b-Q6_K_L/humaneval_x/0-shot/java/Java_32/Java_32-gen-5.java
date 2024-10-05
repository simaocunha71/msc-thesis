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

        // Initialize the lower and upper bounds for the bisection method
        double low = 0;
        double high = 1;

        // Initialize the precision for the bisection method
        double precision = 0.0001;

        // Calculate the value of the polynomial at the lower and upper bounds
        double lowValue = poly(xs, low);
        double highValue = poly(xs, high);

        // If the polynomial value at the lower bound is negative, swap the bounds
        if (lowValue < 0) {
            double temp = low;
            low = high;
            high = temp;
            double tempValue = lowValue;
            lowValue = highValue;
            highValue = tempValue;
        }

        // If the polynomial value at the lower bound is positive, return 0
        if (lowValue > 0) {
            return 0;
        }

        // If the polynomial value at the upper bound is negative, return 1
        if (highValue < 0) {
            return 1