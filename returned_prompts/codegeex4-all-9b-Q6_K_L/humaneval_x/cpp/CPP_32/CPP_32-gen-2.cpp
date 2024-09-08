The function `find_zero` should return the zero point of the polynomial represented by the coefficients `xs`. The function should use the `poly` function to evaluate the polynomial at different points and find the point where the polynomial equals zero.

Here is the corrected code:

```cpp
double find_zero(vector<double> xs){
    double x = -1.0;
    double step = 0.01;
    while (poly(xs, x) != 0){
        x += step;
    }
    return x;
}
```

This code uses a simple iterative approach to find the zero point. It starts with an initial value of `x` and increments it by a small step (`step`) until the polynomial evaluates to zero. The step size can be adjusted to speed up or slow down the search for the zero point.

Note that this is a simple implementation and may not be the most efficient or accurate method for finding the zero point of a polynomial. For more accurate and efficient methods, you may want to look into numerical methods for finding roots of polynomials, such as the Newton-Raphson method or the bisection method.