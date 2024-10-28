The code you have is correct and should work as expected. However, you did not mention the method you used to find the zeros of the polynomial. Here are some methods you can use to find the roots of a polynomial:

1. Newton-Raphson method: This method is used to find the root of a function. It uses the formula: x(n+1) = x(n) - f(x(n))/f'(x(n)). Here, f'(x(n)) is the derivative of the function at x(n).

2. Bisection method: This method is used to find the roots of a function in an interval. It uses the formula: x = (a + b)/2, where a and b are the endpoints of the interval. If f(x) has different signs at a and b, then the root lies in the interval (a, b).

3. Horner's method: This method is used to evaluate a polynomial at a point. It uses the formula: p(x) = ((x - a1)*(x - a2)*...*(x - an))/(bn). Here, an and bn are the coefficients of the polynomial.

4. Cramer's rule: This method is used to solve a system of linear equations. It uses the formula: x = (Ad - bc)/(da - bc), where A, B, C are the coefficients of the system of equations.

Note: The code you have is a correct implementation of the Horner's method for evaluating a polynomial.

Remember that the Newton-Raphson method and the Bisection method are more advanced methods and may require more computations than the Horner's method.

Also, the Horner's method is more efficient than the other methods for evaluating a polynomial at a point. However, the other methods can be useful in certain situations.

In conclusion, the method you use to find the roots of a polynomial depends on the specific requirements of your problem.

Here is the modified code using Newton-Raphson method:

```cpp
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

double poly(vector<double> xs, double x){
    double sum=0;
    for (int i=0