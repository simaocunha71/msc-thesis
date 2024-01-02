/*
This function takes two positive numbers x and y and returns the
biggest even integer number that is in the range [x, y] inclusive. If 
there's no such number, then the function should return -1.

For example:
choose_num(12, 15) = 14
choose_num(13, 12) = -1
*/
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
	if(x>=y) return -1;
	if (x>=0 && y>=0 && x<=0 && y<=0)return 0;
	//int x=x/2,y=y/2;
	int i=x-1;
	int j=(i+y)/2;
	while(j>i){
		if(i<j&&j%2==0)return j*2;
		else{
			i+=2;
			j=i/2;}
	}
	return -1;
}
int main(){
	int a,b,c;
	scanf("%d %d",&a,&b);
	printf("%d\n",choose_num(a,b));
}