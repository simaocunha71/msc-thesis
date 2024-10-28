#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

bool check_prime(int n)
{
    if(n<=1)
    return false;
    for(int i=2;i*i<=n;i++)
    {
        if(n%i==0)
        return false;
    }
    return true;
}

vector<int> generate_prime(int start, int end)
{
    vector<int> primes;
    for(int i=start;i<=end;i++)
    {
        if(check_prime(i))
        primes.push_back(i);
    }
    return primes;
}

int main()
{
    int start,end;
    printf("Enter start of range: ");
    scanf("%d",&start);
    printf("Enter end of range: ");
    scanf("%d",&end);
    vector<int> primes=generate_prime(start,end);
    printf("Prime numbers in range are: ");
    for(int i=0;