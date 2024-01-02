/*
Complete the function that takes two integers and returns 
the product of their unit digits.
Assume the input is always valid.
Examples:
multiply(148, 412) should return 16.
multiply(19, 28) should return 72.
multiply(2020, 1851) should return 0.
multiply(14,-15) should return 20.
*/
#include<stdio.h>
#include<math.h>
using namespace std;
int multiply(int a,int b){
    int temp=a*b;
    if (temp == 9)
        return 9;
    else
        {
        return temp%10;}
}
int main(){
	system("cls");
	int i,j,x,y;
	scanf("%d",&x);
	scanf("%d",&y);
	//printf("%d\n",multiply(x,y));
    int i=x,j=y;
	if (i==-1 || j==-1)
        return 0;
    else if ((i>9 && i!=0)||(j<10 && j!=0))
        {
        printf("Invalid Input\n");
        return 0;}
    x=pow(10,i);
	y=pow(10,j);
	printf("%d",pow(x,y));
	return 0;
}
