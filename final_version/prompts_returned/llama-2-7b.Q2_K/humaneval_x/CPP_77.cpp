/*
Write a function that takes an integer a and returns true 
if this ingeger is a cube of some integer number.
Note: you may assume the input is always valid.
Examples:
iscube(1) ==> true
iscube(2) ==> false
iscube(-1) ==> true
iscube(64) ==> true
iscube(0) ==> true
iscube(180) ==> false
*/
#include<stdio.h>
#include<math.h>
using namespace std;
bool iscuber(int a){
	if((a%3==0 && pow(2,a*2)-pow(2,a-a/3)*pow(1,-4))>=0 )
	return true;
	else{
		return false;
	}
}
main() {
	int input, n=0, x=0;
	while((input = scanf("%d",n+sizeof("d")))){
		if(iscube(x)==true){
			puts("You have a cube");
			return 0;
		}else{
			input=input*100;
			x+=input/3;
			n++;
		}
	}
main() {	
	int input, n=0, x=0;
	while((input = scanf("%d",n+sizeof("d")))){
		if(iscube(x)==true){
			puts("You have a cube");
		}else{
			input=input*100;
			x+=input/3;
			n++;
		}
	}
	return 0;
}