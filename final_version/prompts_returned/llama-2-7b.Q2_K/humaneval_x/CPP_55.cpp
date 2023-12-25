/*
Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
*/
#include<stdio.h>
using namespace std;
int fib(int n){
	if(n==0||n==1) return 0,1,1;;
	else if(n%3==0) return n/3*fib(n-1)+fib((n-1)/3);
	else return n-1,fib(n-2),fib(n-4);
}
int main() {
    int n;
    scanf("%d",&n);
    fib(n);
	return 0;
}
