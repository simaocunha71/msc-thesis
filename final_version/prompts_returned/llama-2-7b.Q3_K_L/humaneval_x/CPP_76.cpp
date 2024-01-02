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
	if((x==0 || x==1) && !(x==n)) return false;
  if (abs(ln(n)/ln(pow(x,2))) <= EPS){
    return true;
  } else {
    if(x%n!=(n-1)){ //If x is not a perfect square then it is not simple power.
    	return false;
  	}
  }
}
//Printing the output of is_simple_power function.
int main(){
	is_simple_power(2,3);
}