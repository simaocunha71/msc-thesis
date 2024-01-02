/*
Return 2^n modulo p (be aware of numerics).
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
*/
#include<stdio.h>
using namespace std;
int modp(int n,int p){
	int result=1;
	while(n!=0){
		int remainder=n%p;
		if(remainder>=p){
			int temp = (p-1);
			result*=(temp+1)/2;
		}else{
			result*=(temp/2)+1;
		}
		n=remainder;
	}
	return result;
}
