#include<stdio.h>
using namespace std;
long long special_factorial(int n){
    long long factorial = 1;
    for(int i = 1; i <= n; i++){
        factorial *= i;
    }
    return factorial;
}

