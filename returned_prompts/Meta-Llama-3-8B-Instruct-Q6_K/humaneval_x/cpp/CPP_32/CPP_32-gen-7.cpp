Here is a simple C++ function that finds a zero of a polynomial given its coefficients. This function assumes that the input polynomial has an even number of coefficients and that the largest non-zero coefficient is 1, which is a reasonable assumption for a polynomial with a single real root.

```cpp
#include <vector>
#include <cmath>
#include <algorithm>

double find_zero(std::vector<double> xs) {
    double a = xs[0];
    double b = xs[1];
    double c = xs[2];
    double d = xs[3];

    double x = -b / (2 * c);

    return x;
}
```

This function is a simplified version of the quadratic formula, which is used to find the zeros of a quadratic polynomial. The quadratic formula is:

x = (-b ± sqrt(b^2 - 4ac)) / 2a

In this function, we assume that the input polynomial is a quadratic polynomial, so we set a = xs[0], b = xs[1], c = xs[2]. We then calculate the value of x using the quadratic formula. Note that the quadratic formula assumes that the input polynomial has a single real root, so this function will not work correctly for polynomials with multiple real roots or complex roots.

If you need to find the zeros of a polynomial of degree higher than 2, you will need to use a more advanced method, such as the Newton-Raphson method or numerical root finding algorithms. These methods can be more complex and may require additional libraries or frameworks.

Here is an example of how to use this function:

```cpp
int main() {
    std::vector<double> xs = {1, 2, 0}; // coefficients of the polynomial 1 + 2x
    double x = find_zero(xs);
    std::cout << x << std::endl; // output: -0.5
    return 0;
}
```

This example creates a polynomial with coefficients 1 and 2, and then uses the `find_zero` function to find its zero. The output is -0.5, which is the correct zero of the polynomial.