/*
Return true if a given number is prime, and false otherwise.
>>> is_prime(6)
false
>>> is_prime(101)
true
>>> is_prime(11)
true
>>> is_prime(13441)
true
>>> is_prime(61)
true
>>> is_prime(4)
false
>>> is_prime(1)
false
*/
#include<stdio.h>
using namespace std;
bool is_prime(long long n){
    bool is_prime = true;
    if(n<=1){
        return false;
    }
    for(int i=2;i<n;i++){
        if(n%i==0){
            is_prime = false;
            break;
        }
    }
    return is_prime;
} 
```



