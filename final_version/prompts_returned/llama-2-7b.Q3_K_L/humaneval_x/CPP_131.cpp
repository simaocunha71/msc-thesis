/*
Given a positive integer n, return the product of the odd digits.
Return 0 if all digits are even.
For example:
digits(1)  == 1
digits(4)  == 0
digits(235) == 15
*/
#include<stdio.h>
#include<string>
using namespace std;
int digits(int n){
	if(n==0) return 0;
	//cout << n << endl;
	int even=0,odd=-1,num=0,remainder=0;
	while(n!=0){
		remainder=(n%10);
		num+=even;
		if(remainder==1) odd++;
		else if(remainder==3) odd--;
		if(odd>-1) even=0,odd=-1;
		else {
			even++,odd=-1;
		}
		n/=10;
	}
	return num*even+odd;
}