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
	if(n<=0||n==1||n==2)
	    return false;
	int i=3;
	while(i*i<n&&n%i!=0)
		++i;
	return (n>=i);
}
