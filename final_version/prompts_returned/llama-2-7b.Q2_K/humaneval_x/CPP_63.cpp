/*
The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
Please write a function to efficiently compute the n-th element of the fibfib number sequence.
>>> fibfib(1)
0
>>> fibfib(5)
4
>>> fibfib(8)
24
*/
#include<stdio.h>
using namespace std;
int fibfib(int n){
	if(n==0||n==1) return 0;
	for(int i=3;i<=n/2;i++){ // i:0,1; j:2,3
		int sum = 0;
		sum += (int)(pow(n,j));
	}
	return sum;
}
int main(){
    printf("hello");
    return 0;
}