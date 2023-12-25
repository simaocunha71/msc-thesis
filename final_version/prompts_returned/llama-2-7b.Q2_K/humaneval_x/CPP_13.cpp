/*
Return a greatest common divisor of two integers a and b
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
*/
#include<stdio.h>
using namespace std;
int greatest_common_divisor(int a, int b){
	if(a == 0 || b == 0 ) return 0;   //when both are zero
	b = abs(b);               //for the negative number -ve
	while(a%b != 0)            //while a is not a multiple of b ,do this.
        a++;                    //so that we can get the next higher multiple of b which will be called a now..
	return a;                   //now return the product
}
int main(){
    int i,a=0,b=0;
     while(scanf("%d %d",&i, &b)==2){
        printf(">>> greatest_common_divisor(%d,%d)\n",i,b);
        a = greatest_common_divisor(i+1,b);
        printf("a = %d\n",a);
    }	
return 0;
}
