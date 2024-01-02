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
	if(a==0 && b==0)
        return a%b;
    else if (b>=a)
            return b%a; 
    else{
    		return greatest_common_divisor(a-1, b);
    }
}
int main(){
	scanf("%d",&n);
	printf("greatest common divisor of %d and %d is: %d\n", n%3, 5, greatest_common_divisor(n%3, 5));  
	return 0;
}