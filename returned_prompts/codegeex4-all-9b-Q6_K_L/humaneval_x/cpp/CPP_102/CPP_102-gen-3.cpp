#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
	if(x%2==0&&x<=y){
		return x;
	}
	else if(x%2==1&&x<=y){
		return x+1;
	}
	else{
		return -1;
	}
}