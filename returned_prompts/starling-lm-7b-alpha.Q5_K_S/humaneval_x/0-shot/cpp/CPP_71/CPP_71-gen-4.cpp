Here's a C++ solution to calculate the area of a triangle:

```cpp
#include <iostream>
#include <cmath>

float triangle_area(float a, float b, float c) {
    if (a < b + c && b < a + c && c < a + b) {
        float s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    } else {
        return -1;
    }
}

int main() {
    std::cout << std::fixed << std::setprecision(2) << triangle_area(3, 4, 5) << std::endl;
    return 0;
}
```

In this code, the `triangle_area` function takes three arguments representing the lengths of the triangle's sides. It first checks if the three sides can form a valid triangle by ensuring that the sum of any two sides is greater than the third side. If the triangle is valid, it calculates the area using Heron's formula. If the triangle is not valid, it returns -1.

In the `main` function, we call `triangle_area` with the lengths of sides 3, 4, and 5, and print the result with two decimal points using `std::fixed` and `std::setprecision`.

The output of the program will be `6.00`, which is the area of the triangle with sides of length 3, 4, and 5.

Note: Make sure to include the necessary header files (`<iostream>` and `<cmath>`) and use the `std