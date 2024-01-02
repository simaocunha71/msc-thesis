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
        for (int i = 0; i < xs.size(); i++) {
            if (xs.get(i) == Double.NEGATIVE_INFINITY || xs.get(i) == Double.POSITIVE_INFINITY)
                return -1; // infinity point not considered
        }
        
        double result = 0;
        int i = 0;
        while (true) {
            for (int j = 1; j < xs.size(); j++) {
                if (xs.get(i) == Double.NEGATIVE_INFINITY || xs.get(i) == Double.POSITIVE_INFINITY ||
                    ((xs.get(j) - xs.get(i)) /