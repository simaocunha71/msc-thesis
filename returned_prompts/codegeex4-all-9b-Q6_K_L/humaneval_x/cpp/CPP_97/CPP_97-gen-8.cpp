/*
Write a program that takes two integers as input and outputs the product of their unit digits.
*/
#include<stdio.h>
#include<math.h>
using namespace std;
int main(){
    int a,b;
    printf("Enter two numbers: ");
    scanf("%d %d",&a,&b);
    int p = (abs(a)%10)*(abs(b)%10);
    printf("The product of unit digits is: %d",p);
    return 0;
}
