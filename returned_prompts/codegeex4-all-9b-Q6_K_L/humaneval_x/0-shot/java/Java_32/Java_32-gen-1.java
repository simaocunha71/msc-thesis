The provided Java code defines a class `Solution` with two methods: `poly` and `findZero`. 

The `poly` method evaluates a polynomial at a given point `x`. It takes a list of coefficients `xs` and a double `x` as arguments. It iterates over the list of coefficients, multiplying each coefficient by `x` raised to the power of the index, and adds the result to `result`. Finally, it returns `result`.

The `findZero` method finds a zero of a polynomial. It takes a list of coefficients `xs` as an argument. It ensures that the list has an even number of elements and that the largest non-zero coefficient is positive. It then uses the `poly` method to evaluate the polynomial at various points until it finds a zero. It returns the zero it finds.

Here is the Java code with some comments added for clarity:

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
        // Ensure the list has an even number of elements
        if (xs.size() % 2 != 0) {
            throw new IllegalArgumentException("List must have an even