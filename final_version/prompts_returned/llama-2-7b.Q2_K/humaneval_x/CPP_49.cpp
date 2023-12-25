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
	if((n%p)>=0&&(n/p)<=9)return (n-1+modp(n-(n-1),p))%p;
	else return n;
}
int main(){
	printf("%d\n",modp(3,5));
}