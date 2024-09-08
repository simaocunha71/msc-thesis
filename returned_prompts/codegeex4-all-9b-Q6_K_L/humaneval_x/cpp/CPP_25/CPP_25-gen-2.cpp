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
    int i = 2;
    vector<int> factors;
    while(i <= n){
        if(n % i == 0){
            factors.push_back(i);
            n = n / i;
        }else{
            i = i + 1;
        }
    }
    return factors;
}

C:
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
    int i = 2;
    vector<int> factors;
    while(i <= n){
        if(n % i == 0){
            factors.push_back(i);
            n = n / i;
        }else{
            i = i + 1;
        }
    }
    return factors;
}

B:
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
    int i = 2;
    vector<int> factors;
    while(i <= n){
        if(n % i == 0){
            factors.push_back(i);
            n = n / i;
       