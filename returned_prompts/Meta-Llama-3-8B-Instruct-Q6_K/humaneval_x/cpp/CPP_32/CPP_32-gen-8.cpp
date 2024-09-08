Here is the code for the function find_zero which evaluates the polynomial at different points and finds the root. Note that this code may not be efficient for large polynomials or large ranges.

```cpp
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;

double find_zero(vector<double> xs) {
    // check if the polynomial has at least 2 coefficients
    if (xs.size() < 2) {
        return -1.0;  // or throw an exception
    }

    // check if the polynomial has an even number of coefficients
    if (xs.size() % 2 != 0) {
        return -1.0;  // or throw an exception
    }

    // check if the largest coefficient is not zero
    double max_coeff = 0.0;
    for (double coeff : xs) {
        if (abs(coeff) > max_coeff) {
            max_coeff = abs(coeff);
        }
    }
    if (max_coeff == 0.0) {
        return -1.0;  // or throw an exception
    }

    // evaluate the polynomial at different points and find the root
    double x = 0.0;
    double tol = 1e-6;  // tolerance for the root
    double max_iter = 1000;  // maximum number of iterations
    double dx = 1.0;  // initial step size
    double sum = 0.0;

    for (int i = 0; i < max_iter; i++) {
        sum = 0.0;
        for (int j = 0; j < xs.size(); j++) {
            sum += xs[j] * pow(x, j);
        }
        if (abs(sum) < tol) {
            return x;
        }
        double deriv = 0.0;
        for (int j = 1; j < xs.size(); j++) {
            deriv += j * xs[j] * pow(x, j - 1);
        }
        x -= sum / deriv;
        if (abs(dx) < tol) {
            break;
        }
        dx = x - sum / deriv;
    }

    return -1.0;  // or throw an exception
}
```

You can test the function with the following code:

```cpp
int main() {
    vector<double> xs1 = {1, 2};  // f(x) = 1