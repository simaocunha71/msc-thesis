/*
Your task is to write a function that returns true if a number x is a simple
power of n and false in other cases.
x is a simple power of n if n**int=x
For example:
is_simple_power(1, 4) => true
is_simple_power(2, 2) => true
is_simple_power(8, 2) => true
is_simple_power(3, 2) => false
is_simple_power(3, 1) => false
is_simple_power(5, 3) => false
*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool is_simple_power(int x,int n){
	if((x==0)||(n==0))return (x==0);
	else return ((fabs(sqrt(1/pow(double(x),2)))>=n-1));
}
main(){
	for(int i=3;i<40000;++i)printf("%d ",is_simple_power(i,i));
}
