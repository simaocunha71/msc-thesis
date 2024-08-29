/*
The Brazilian factorial is defined as:
brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
where n > 0

For example:
>>> special_factorial(4)
288

The function will receive an integer as input and should return the special
factorial of this integer.
*/
#include<stdio.h>
#include<math.h>
using namespace std;
long long special_factorial(int n){
    long long result = 1;
    for(int i = n; i > 0; i--){
        result *= factorial(i);
    }
    return result;
}
long long factorial(int n){
    if(n == 0){
        return 1;
    }
    return n * factorial(n-1);
}

C:
/*
The Brazilian factorial is defined as:
brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
where n > 0

For example:
>>> special_factorial(4)
288

The function will receive an integer as input and should return the special
factorial of this integer.
*/
#include<stdio.h>
#include<math.h>
using namespace std;
long long special_factorial(int n){
    long long result = 1;
    for(int i = n; i > 0; i--){
        result *= i;
        result *= factorial(i);
    }
    return result;
}
long long factorial(int n){
    if(n == 0){
        return 1;
    }
    return n * factorial(n-1);
}

D:
/*
The Brazilian factorial is defined as:
brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
where n > 0

For example:
>>> special_factorial(4)
288

The function will receive an integer as input and should return the special
factorial of this integer.
*/
#include<stdio.h>
#include<math.h>
using namespace std;
long long special_factorial(int n){
    long long result = 1;
    for(int i = n; i > 0; i--){
        result *= i;
        result *= factorial(i-1);
    }
    return result;
}
long long factorial(int n){
    if(n == 0){
        return 1;
    }
    return n * factorial(n-1);
}

E:
/*
The Brazilian factorial is defined as:
