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
    if(n==0)
        return 0;
    if(n==1)
        return 0;
    if(n==2)
        return 2;
    if(n==3)
        return 0;
    int fib0=0,fib1=0,fib2=2,fib3=0;
    for(int i=4;i<=n;i++){
        int temp=fib0+fib1+fib2+fib3;
        fib0=fib1;
        fib1=fib2;
        fib2=fib3;
        fib3=temp;
    }
    return fib3;
}
int main(){
    for(int i=0;i<10;i++)
        printf("%d ",fib4(i));
    printf("\n");
    return 0;
}

