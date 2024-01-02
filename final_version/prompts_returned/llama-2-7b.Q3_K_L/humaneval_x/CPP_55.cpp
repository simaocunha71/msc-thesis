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
	if(n==0 || n==1) return 1;
	for(int i=2;i<=n-1;i++){
		if(i>=2 && i%2!=0) break;
		else printf("%d\n", fib(i-1)+fib(i-2));
	}
}
//Driver Code
int main(){
	int n,i;
	scanf("%d",&n);
	printf("fib(%d)\n", fib(n));
	return 0;
}
