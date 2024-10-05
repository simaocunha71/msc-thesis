The function findZero uses the bisection method to find the root of the polynomial. 

The bisection method is a root-finding method that applies to any continuous function for which one knows two values with opposite signs. The method consists of repeatedly bisecting the interval and then selecting the sub-interval in which the function changes sign.

In this case, the polynomial is f(x) = xs[0] ​​ + xs[1] * x ​​ + xs[2] * x^2 ​​ + ... + xs[n] * x^n, and the function f(c) is used to test the midpoint of the interval (a + b)/2. 

If f(c) is close to zero, then the bisection method has converged to the root. If not, then the root is in the interval from a to b or from b to a, depending on the sign of f(a) and f(b). 

So, in the while loop, if f(c) is close to zero, we break the loop. If not, we adjust our interval a or b accordingly and continue the loop. 

This process continues until f(c) is close enough to zero. 

The final value of c is the approximate root of the polynomial.

The precision of the method is determined by the size of the interval [a, b] at the start of the method, which is set to [a=-10, b=10] in this case.

The method assumes that the polynomial has at least one root in the interval [a, b], and that the signs of f(a) and f(b) are opposite. If these assumptions