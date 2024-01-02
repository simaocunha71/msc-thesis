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
	if(n<=2) return false;
	for (int i=2;i<n/2+1;i++){
        if(n%i==0){
            printf("n is divisible by %ld\n",i);
            return false;
        }
    }
return true;
}
main(){
	long long n=6;
	if(is_prime(n)){
		printf("%d is prime!\n",n);
	}else{
		printf("%d is not prime\n",n);
	}
}