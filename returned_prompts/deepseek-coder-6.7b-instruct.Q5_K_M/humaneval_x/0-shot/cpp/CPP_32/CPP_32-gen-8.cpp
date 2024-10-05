The problem is with the function find_zero. The implementation of the Newton-Raphson method for finding roots of a function is not provided in the question.

The Newton-Raphson method is a way to find approximate solutions to equations iteratively. Given a function f(x), the next guess x1 is computed as:

x1 = x0 - f(x0)/f'(x0)

where f'(x0) is the derivative of the function at x0.

Here is the implementation of the Newton-Raphson method:

```cpp
double find_zero(vector<double> xs, double x0 = 0.0, double eps = 1e-6){
    auto f = [&](double x) { return poly(xs, x); };
    auto df = [&](double x) { 
        double sum = 0;
        for (int i = 1; i < xs.size(); i++) {
            sum += i * xs[i] * pow(x, i - 1);
        }
        return sum;
    };

    while (fabs(f(x0)) > eps){
        x0 = x0 - f(x0) / df(x0);
    }

    return x0;
}
```

This function takes the coefficients of the polynomial as input, the initial guess as the optional second argument (default is 0.0), and the desired precision as the optional third argument (default is 1e-6). The function returns the root of the polynomial.

Please note that this function does not check if the initial guess is a good approximation of the root or if the derivative of the polynomial at the initial guess is non-zero. You may want to add these checks if you use this function in a production environment.

Also, the Newton-Raphson method may not converge for some polynomials and starting points, and it may get stuck in an infinite loop. If you are sure that the method will converge, you can increase the precision eps to a higher value.

Here is an example of how to use the function:

```cpp
int main(){
    vector<double> xs = {-6, 11, -6, 1};
    double root = find