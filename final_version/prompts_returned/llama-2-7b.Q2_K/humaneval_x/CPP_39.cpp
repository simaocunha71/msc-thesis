/*
prime_fib returns n-th number that is a Fibonacci number and it's also prime.
>>> prime_fib(1)
2
>>> prime_fib(2)
3
>>> prime_fib(3)
5
>>> prime_fib(4)
13
>>> prime_fib(5)
89
*/
#include<stdio.h>
using namespace std;
int prime_fib(int n){
	if(n==0||n==1)return 1;
        int f=2,p=0,a=1;
    while((p<n-1)&&(!(a%p))){
            a=(f+a);f=f*a-f*p;printf("%d ",a);p++;}
	return 0;
}
int main(){
	for(int i=1;;i++){
        if(prime_fib(i)!=0)puts("yes");
    else{puts("no");break;}
    }
   return 0;
}
