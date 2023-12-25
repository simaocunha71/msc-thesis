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
	if((x+y)>0 && (x-1) >0 )
	{
	for(int i=x-(x+y);i>=y;i--)
		printf("%d ",i%2==0?i:(-1));
	}
	else  return -1;

	return 0;
}
int main(){
    choose_num(8,64);
	choose_num(13,14);
	system("pause");
	return 0;
}
