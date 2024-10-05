    vector<int> primes;
    vector<int>::iterator it;
    int i, j, isPrime;

    for(i = 2; i < *max_element(lst.begin(), lst.end()); i++){
        isPrime = 0;
        for(j = 2; j <= i/2; ++j){
            if(i % j == 0){
                isPrime = 1;
                break;
            }
        }
        if(isPrime == 0){
            primes.push_back(i);
        }
    }

    int maxPrime = *max_element(primes.begin(), primes.end());
    int sum = 0;
    while(maxPrime != 0){
        sum += maxPrime % 10;
        maxPrime /= 10;
    }
    return sum;
}

I was thinking of a function that will check if the numbers in the list are prime, then find the maximum prime number in the list and add its digits together. However, I am not sure how to implement this in C++.

A: Here is the C++ code:

#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
bool isPrime(int n)
{
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
    for (int i = 5; i * i <= n; i = i + 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}
int sumOfDigits(int n)
{
    int sum = 0;
    while (n != 0)
    {
        sum = sum + n % 10;
        n = n / 10;
    }
    return sum;
}
int largestPrimeSum(vector<int> numbers)
{
    int maxPrime = -1;
    for (int i = 0; i