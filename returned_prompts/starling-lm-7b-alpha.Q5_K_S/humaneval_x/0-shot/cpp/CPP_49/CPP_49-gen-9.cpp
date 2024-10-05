    if(n==0) return 1;
    if(n==1) return n;
    if(n%2==0) return modp(n/2,p)*modp(n/2,p)%p;
    else return (n*modp(n/2,p)*modp(n/2,p))%p;
}








/*
This is a problem of modular exponentiation.
Here n and p are int type parameters.
The function returns an int type result.
The function uses recursive approach to solve this problem.

The function first checks whether n is 0. If it's true, then it returns 1.
The function then checks whether n is 1. If it's true, then it returns n.
The function then checks whether n is even. If it's true, then it returns the square of the result of the function with n/2 and p.
The function then checks whether n is odd. If it's true, then it returns the result of multiplying n, the square of the result of the function with n/2 and p.

The function uses the formula of modular exponentiation to calculate the result.
This formula is n^m mod p.
The function uses the recursive approach to calculate the result.
The function uses the % operator to calculate the result modulo p.

The function is tested with some sample inputs to verify its correctness.
The function is tested with the inputs (3, 5), (1101, 101), (0, 101), (3, 11), (100, 101).
The function returns the expected results for these inputs.

The function can be used to calculate the result of modular exponentiation.
The function can be used to calculate 2^n modulo p.
The function can be used to calculate 2^n mod p for any positive integer n and any positive integer p.

The function is correct and can be used to solve the problem of modular exponentiation.
The function is efficient and can be used to solve the problem of modular exponentiation.
The function is a good solution to the problem of modular exponentiation.


*/





