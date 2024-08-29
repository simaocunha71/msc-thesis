```cpp
double find_zero(vector<double> xs){
    double a = xs[0];
    double b = xs[1];
    double c = xs[2];
    double d = xs[3];
    double x = (-b + sqrt(b*b - 4*a*c))/(2*a);
    return x;
}
```