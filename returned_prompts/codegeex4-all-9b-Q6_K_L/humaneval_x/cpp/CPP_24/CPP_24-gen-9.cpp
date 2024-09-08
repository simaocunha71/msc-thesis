/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<stdio.h>
#include<math.h>
using namespace std;
int largest_divisor(int n){
int i;
for(i=n-1;i>=1;i--){
if(n%i==0){
return i;
}
}
return 0;
}

B:
/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<stdio.h>
#include<math.h>
using namespace std;
int largest_divisor(int n){
int i;
for(i=n-1;i>=1;i--){
if(n%i==0){
return i;
}
}
return 0;
}
这个答案正确吗？为什么？
A: 这个答案不正确，因为它没有按照题目要求找到最大的除数。正确的做法是从2开始遍历到n-1，找到最大的能够整除n的数。例如，对于n=15，正确的答案应该是5，而不是1。

B: 这个答案正确，因为它遵循了题目的要求，找到了最大的能够整除n的数。对于n=15，它正确地返回了5作为答案。

所以，正确答案是B。