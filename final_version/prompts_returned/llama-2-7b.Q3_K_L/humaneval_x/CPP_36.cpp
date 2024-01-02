/*
Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
*/
#include<stdio.h>
using namespace std;
int fizz_buzz(int n){
	int counter=0,count=0;
	if (n <= 10) {
	for (int i = 0;i<=n;++i){
		if (i % 13 == 0 && i % 11 != 0){
		    ++counter;
            printf("%d ",i);
        }else if(i%7==0){
        	printf("fizz");
        }else{
    	    printf("buzz");
        }
}
	}
	return counter;
}
int main(){
	int n = 50,counter = fizz_buzz(n);
	printf("%d",counter);
	return 0;
}