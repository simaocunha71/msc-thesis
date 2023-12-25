/*
A simple program which should return the value of x if n is 
a prime number and should return the value of y otherwise.

Examples:
for x_or_y(7, 34, 12) == 34
for x_or_y(15, 8, 5) == 5

*/
#include<stdio.h>
using namespace std;
int x_or_y(int n,int x,int y){
	if(n==0||n%x==0){
      printf("%d is not a prime number and %d is its multiple!",x);
    }else{
      if((n+1)%x==0){
      	printf("%d plus one is not a prime number, but it multiple is %d!",(n+1),y);
    	return  y;
  	}else{
  		printf("%d has no other multiple except %d and itself!",x,x);
    }

}
main(){
	int n, x, y;
	scanf("%d",&n);
	if(n==0){
		printf("This is zero!");
	}else{
		scanf("%d %d", &x, &y);
	  	printf("\n");
    	x_or_y(n,x,y);
	}
}
