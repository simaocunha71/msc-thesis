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
    if(n==2)return true;
    if(n==1)return false;
    for(int i=2;i<n/2;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}
请问这个代码有什么问题，给出改正后的代码

