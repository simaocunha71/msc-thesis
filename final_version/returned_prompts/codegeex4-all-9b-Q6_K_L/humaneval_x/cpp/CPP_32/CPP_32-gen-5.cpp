```cpp
double find_zero(vector<double> xs) {
    double x = 0;
    double step = 0.01;
    while (poly(xs, x) != 0) {
        x += step;
    }
    return x;
}
```

This function finds a zero of the polynomial by incrementing x by a small step until the polynomial evaluates to 0. The step size can be adjusted for more accuracy.