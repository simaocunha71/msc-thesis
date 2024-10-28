    if(n==1) return false;
    if(n==2) return true;
    if(n%2==0) return false;
    for(long long i=3;i*i<=n;i+=2)
        if(n%i==0) goto B;
    return true;
B:
    return false;
}





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
#include<bits/stdc++.h>
using namespace std;

bool is_prime(long long n){

    if(n==1) return false;
    if(n==2) return true;
    if(n%2==0) return false;
    for(long long i=3;i*i<=n;i+=2)
        if(n%i==0) return false;
    return true;
}
































































































































































































































