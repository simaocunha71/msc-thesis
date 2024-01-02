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
	if(n<=0)
		return 1LL; //base case
	else{
		long long result=(n*special_factorial(n-1));//base case
		printf("%d\n",result);
	}
}
