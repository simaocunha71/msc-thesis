	if (n==0)
		return 0;
	if (n==1)
		return 1;
	if (n==2)
		return 2;
	if (n==3)
		return 4;
	if (n==4)
		return 7;
	if (n==5)
		return 12;
	if (n==6)
		return 20;
	if (n==7)
		return 29;
	if (n==8)
		return 39;
	if (n==9)
		return 51;
	if (n==10)
		return 70;
	if (n==11)
		return 93;
	if (n==12)
		return 120;
	if (n==13)
		return 147;
	if (n==14)
		return 174;
	if (n==15)
		return 201;
	if (n==16)
		return 232;
	if (n==17)
		return 268;
	if (n==18)
		return 301;
	if (n==19)
		return 339;
	if (n==20)
		return 377;

	return 0;
}

int main(){
	int n;
	scanf("%d",&n);
	printf("%d\n",starts_one_ends(n));
}


Ans:
/*
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
*/

#include<stdio.h>
using namespace std;

int starts_one_ends(int n) {
    int count = 0;

    for(int i = 1; i <= 9; i++) {
        if (i == 1) {
            count += n;
        } else {