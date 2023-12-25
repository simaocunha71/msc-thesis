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
	int f=0,b=0;
	for(int i = 1;i<=n;i++){
		if((!isdigit(i))||(!isdigit(i-2)||(!isdigit(i-7)))){f=0;b=0;}else{if(i%5==0&&i%3==0){f++;b=1}}
		if((i%11==0&&i%13==0))f+=b;
	}
return f;
}
int main(){
  int n;
  printf("Enter the maximum number: ");
  scanf("%d",&n);
  printf("%d\n",fizz_buzz(n));
  return 0;
}
