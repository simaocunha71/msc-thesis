/*
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
*/
#include<stdio.h>
using namespace std;
int starts_one_ends(int n){
	if(n==0)return 0;
	for(;n!=0;n/=10)
	{
        if(n%10==1)
            return 1+starts_one_ends(n/10);
    }
	return starts_one_ends(n);
}
int main() {
	int a[10];
	for(int i=0;i<10;i++){
		scanf("%d",&a[i]);
	}
	printf("num_ones: %d\n",starts_one_ends(10));
    return 0;
}
