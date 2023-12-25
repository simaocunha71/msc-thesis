/*
Create a function that takes 3 numbers.
Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
Returns false in any other cases.

Examples
any_int(5, 2, 7) ➞ true

any_int(3, 2, 2) ➞ false

any_int(3, -2, 1) ➞ true

any_int(3.6, -2.2, 2) ➞ false



*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool any_int(float a,float b,float c){
	if(a==b+c||b==c+a||abs(b-a)<=10|abs(c-a)<=10 ){
		return true;
	}else{
		return false;
	}
}
int main(){
    float a,b,c;
    int flag=0;//0 means no and 1 means yes
    printf("Enter any integer number in any format: ");
    scanf("%d",&a);  
    printf("Enter any integer number in any format: ");
    scanf("%d",&b);
    printf("Enter any integer number in any format: ");
    scanf("%d",&c);    
	flag=any_int(a,b,c);
}