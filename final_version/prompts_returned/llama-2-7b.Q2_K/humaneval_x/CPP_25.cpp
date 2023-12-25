/*
Return vector of prime factors of given integer in the order from smallest to largest.
Each of the factors should be vectored number of times corresponding to how many times it appeares in factorization.
Input number should be equal to the product of all factors
>>> factorize(8)
{2, 2, 2}
>>> factorize(25)
{5, 5}
>>> factorize(70)
{2, 5, 7}
*/
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> factorize(int n){
	vector<int> prime_factors;
	if(!n/1){prime_factors.push_back(1); return prime_factors;}
	while(true){
		if(!n%1) break;
		else{
			prime_factors.push_back((int)floor(log10(n)/(int)log10(4)));
		}
	}
	return prime_factors;
}
