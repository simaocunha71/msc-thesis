	if(n == 0){
		return 1;
	}else if(n % 2 == 0){
		int t = modp(n/2,p);
		return (t*t) % p;
	}else if(n % 2 == 1){
		int t = modp(n-1,p);
		return (t * n) % p;
	}
}






/*
Given an array a and an integer k, return an array b such that b[i] = a[i] + a[i + k] + ... + a[min(i + k - 1, len(a) - 1)].
>>> summation(range(1, 5), 2)
[3, 6, 10, 15, 21]
>>> summation(range(10), 0)
[10]
>>> summation(range(1, 5), 5)
[4, 9, 14, 19, 24]
*/
#include<stdio.h>
using namespace std;
int summation(int *a, int k){
