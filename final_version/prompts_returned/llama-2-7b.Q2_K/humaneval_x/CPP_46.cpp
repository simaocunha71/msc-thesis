/*
The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
fib4(0) -> 0
fib4(1) -> 0
fib4(2) -> 2
fib4(3) -> 0
fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
>>> fib4(5)
4
>>> fib4(6)
8
>>> fib4(7)
14
*/
#include<stdio.h>
using namespace std;
int fib4(int n){
	if(n==0||n==1) return 0;
    int val[3]={0,2},i=0; //initialize fibonacci series to (0,2)
	for(int j=1;j<n-2;j++)//fibonacci sequence of length n-(1)-2
	{
		if(i==j) return val[i];
		else if(val[++i]<val[j]){
			val[i]=val[j]+val[++i]+val[++i];
		} else {
			val[i]=val[j]+val[++i]+val[++i];
		}
	}
    return 0; //if n==3 then the fibonacci sequence is (0,2) = 4 which is 0 as per the function defination.Hence we return it as a default value for n=5 and n-2 values as well.
	return val[j];
}
int main() {
  int n;

  scanf("%d",&n);

  printf("%d\n", fib4(5));
}
