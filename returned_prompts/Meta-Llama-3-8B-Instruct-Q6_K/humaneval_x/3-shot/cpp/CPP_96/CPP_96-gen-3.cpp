    vector<int> primes;
    for (int i=2;i<n;i++)
    {
        bool is_prime=true;
        for (int j=2;j*j<=i;j++)
        {
            if (i%j==0)
            {
                is_prime=false;
                break;
            }
        }
        if (is_prime)
        {
            primes.push_back(i);
        }
    }
    return primes;
}
// Alternative solution using Sieve of Eratosthenes algorithm
#include<stdio.h>
#include<vector>
#include<math.h>
using namespace std;
vector<int> count_up_to(int n){
    vector<bool> is_prime(n+1, true);
    is_prime[0]=is_prime[1]=false;
    for (int i=2;i*i<=n;i++)
    {
        if (is_prime[i])
        {
            for (int j=i*i;j<=n;j+=i)
            {
                is_prime[j]=false;
            }
        }
    }
    vector<int> primes;
    for (int i=2;i<n;i++)
    {
        if (is_prime[i])
        {
            primes.push_back(i);
        }
    }
    return primes;
} 
// Alternative solution using trial division
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> count_up_to(int n){
    vector<int> primes;
    for (int i=2;i<n;i++)
    {
        bool is_prime=true;
        for (int j=2;j*j<=i;j++)
        {
            if (i%j==0)
            {
                is_prime=false;
                break;
            }
        }
        if (is_prime)
        {
            primes.push_back(i);
        }
    }
    return primes;
}
// Alternative solution using wheel factorization
#include<stdio.h>
#include<vector>
using namespace std;
vector<int> count_up_to(int n){
    vector<int> primes;
    bool is_prime[30];
    for (int i=0;i<30;i++)
    {
        is_prime[i]=true;
    }
    is_prime[0]=is_prime[4]=is_prime[6]=is_prime[9]=is_prime[10]=is_prime[16]=is_prime[18]=is_prime[22]=is_prime[24]=is_prime[26]=false;
    for (int i=2;i*i<=n;i++)
    {
        if (is_prime[i])
        {
            for (int j=i*i;j<=n;j