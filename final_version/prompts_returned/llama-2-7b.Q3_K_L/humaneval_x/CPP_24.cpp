/*
For a given number n, find the largest number that divides n evenly, smaller than n
>>> largest_divisor(15)
5
*/
#include<stdio.h>
using namespace std;
int largest_divisor(int n){
	int divisors[n+1];
	int k=1;
	for(int i=0;i<=n;++i)
	{
		if(i%k==0 && i!=k)
			divisors[k]=i;
		else if((i%k)>=0 && i!=k)
			divisors[k]=(i%k)+1;
	}
	for(int i=2;i<=n/2+1;++i)
	{
		if(n%i==0 && n !=i)
			return i;
	}
	return 0;
}
int main(){
	printf("%d",largest_divisor(15));
	return 0;
}