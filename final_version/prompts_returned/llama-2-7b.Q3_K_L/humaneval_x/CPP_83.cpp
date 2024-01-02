/*
Given a positive integer n, return the count of the numbers of n-digit
positive integers that start or end with 1.
*/
#include<stdio.h>
using namespace std;
int starts_one_ends(int n){
	if(n==0)
		return 0;
	for( int i=1;i<=n ;++i){
	    if( (i%2) == 0 && i !=1 )
	    	continue;
	     else
	        return i;
}
int main() {
	int n = 10000;
	int ret_val = starts_one_ends(n);
	printf("%d\n",ret_val) ;
	return 0;
}