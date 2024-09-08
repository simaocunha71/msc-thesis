    vector<float> result(xs.size()-1);
    for(int i = 1; i < xs.size(); i++){
        result[i-1] = i * xs[i];
    }
    return result;
}

int main(){
    vector<float> xs = {3, 1, 2, 4, 5};
    vector<float> result = derivative(xs);
    for(int i = 0; i < result.size(); i++){
        printf("%f ", result[i]);
    }
    return 0;
}
```

Solution:
Here is the C++ code for the problem:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<float> derivative(std::vector<float> xs) {
    std::vector<float> result(xs.size() - 1);
    for (int i = 1; i < xs.size(); i++) {
        result[i - 1] = i * xs[i];
    }
    return result;
}

int main() {
    std::vector<float> xs = {3, 1, 2, 4, 5};
    std::vector<float> result = derivative(xs);
    for (int i = 0; i < result.size(); i++) {
        std::cout << result[i] << " ";
    }
    return 0;
}
```

The `derivative` function takes a vector of coefficients `xs` representing a polynomial, and returns a new vector representing the derivative of the polynomial. The derivative is calculated as the product of the coefficient and its power, for each term in the polynomial.

In the `main` function, we create a vector `xs` representing the polynomial `3 + x + 2x^2 + 4x^3 + 5x^4`, and then call the `derivative` function to calculate its derivative. The result is printed to the console.

Note that the derivative is calculated using the rule of differentiation for polynomials, which states that the derivative of `ax^n` is `n*ax^(n-1)`. In this implementation, we iterate over the terms of the polynomial, and for each term, we multiply the coefficient by its power to get the derivative. The resulting derivative is stored in a new vector, which is then returned by the function.