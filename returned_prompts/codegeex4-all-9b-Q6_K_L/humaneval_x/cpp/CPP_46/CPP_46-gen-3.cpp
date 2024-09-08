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
  if(n == 0 || n == 1 || n == 2 || n == 3){
    return 0;
  }
  int a = 0, b = 0, c = 2, d = 0, e;
  for(int i = 4; i <= n; i++){
    e = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = e;
  }
  return e;
}