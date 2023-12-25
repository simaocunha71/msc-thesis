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
	if(n==0||n==1)
		return n!
	else{
		long double temp=special_factorial(n-1);//calcula factorial do parcial
		temp=(long double)(n*temp);//faz cálculo
	}
	return temp;//devolve o resultado calculado
}
int main(){
	printf("%d!\n",special_factorial(4));
    return 0;
}