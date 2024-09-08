#include<stdio.h>
using namespace std;
int largest_prime_factor(int n){
    int i;
    for (i=2;i<=n;i++){
        if (n%i==0){
            n=n/i;
            i=1;
        }
    }
    return n;
}

