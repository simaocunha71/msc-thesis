```cpp
#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;

double poly(vector<double> xs, double x) {
    double sum = 0;
    for (int i = 0; i < xs.size(); i++) {
        sum += xs[i] * pow(x, i);
    }
    return sum;
}

double find_zero(vector<double> xs) {
    double x = 0;
    double step = 0.01;
    while (poly(xs, x) != 0) {
        x += step;
    }
    return x;
}

int main() {
    vector<double> coefficients1 = {1, 2};
    printf("Zero: %f\n", find_zero(coefficients1));

    vector<double> coefficients2 = {-6, 11, -6, 1};
    printf("Zero: %f\n", find_zero(coefficients2));

    return 0;
}
```