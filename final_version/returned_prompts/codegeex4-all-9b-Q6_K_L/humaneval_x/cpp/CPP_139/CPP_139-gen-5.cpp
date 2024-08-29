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
using namespace std;
long long special_factorial(int n){
    long long int result = 1;
    for(int i = 1; i <= n; i++){
        long long int temp = 1;
        for(int j = 1; j <= i; j++){
            temp *= j;
        }
        result *= temp;
    }
    return result;
}

B:
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
using namespace std;
long long special_factorial(int n){
    long long int result = 1;
    for(int i = 1; i <= n; i++){
        long long int temp = 1;
        for(int j = 1; j <= i; j++){
            temp *= j;
        }
        result *= temp;
    }
    return result;
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
using namespace std;
long long special_factorial(int n){
    long long int result = 1;
    for(int i = 1; i <= n; i++){
        long long int temp = 1;
        for(int j = 1; j <= i; j++){
            temp *= j;
        }
        result *= temp;
    }
    return result;
}

D:
/*
The Brazilian factorial is defined as:
brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1