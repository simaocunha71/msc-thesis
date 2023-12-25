/*
Return the largest prime factor of n. Assume n > 1 and is not a prime.
>>> largest_prime_factor(13195)
29
>>> largest_prime_factor(2048)
2
*/
#include<stdio.h>
using namespace std;
int largest_prime_factor(int n){
	if(n==1||n==2||n==3) return n;
	else if(n % 2 == 0&&n != 6 &&n != 8 )return 2;
	else if(n % 3 == 0)return 3;
	int divisors = 0;
	for (int i=1;i<=n/4;++i){
		if(n%i==0){divisors+=i;}
	}
	if((divisors&2) == 0||(divisors&3) == 0)return divisors + 2;//checking for even and odd numbers.
	else return divisors+1;
}
int main(){
	//printf("\nEnter the number:\n");
	for (int i=1,j = n=4096;i<j;++i)if(largest_prime_factor(n) != -1)j-= largest_prime_factor(n);else printf("Enter an integer between 2 to 100");
	return 0;
}