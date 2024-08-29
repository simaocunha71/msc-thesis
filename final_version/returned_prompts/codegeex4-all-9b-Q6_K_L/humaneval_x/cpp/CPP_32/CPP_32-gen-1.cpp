#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
double poly(vector<double> xs, double x){
    /* 
    Evaluates polynomial with coefficients xs at point x. return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n 
    */
    double sum=0;
    int i;
    for (i=0;i<xs.size();i++)
    {
        sum+=xs[i]*pow(x,i);
    }
    return sum;
}

double find_zero(vector<double> xs){
    /*
    xs are coefficients of a polynomial. find_zero find x such that poly(x) = 0. find_zero returns only only zero point, even if there are many. 
    Moreover, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) #f(x) = 1 + 2x 
    -0.5 
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3 
    1.0
    */
    double x0 = 0, x1 = 0;
    double f0 = poly(xs, x0);
    double f1 = poly(xs, x1);
    while (fabs(f0) > 1e-6) {
        x0 = x1;
        f0 = f1;
        x1 = x0 - f0 / poly(xs, x0);
        f1 = poly(xs, x1);
    }
    return x1;
}