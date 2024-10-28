    vector<int> primes;
    for (int i=2;i<n;i++){
        bool is_prime=true;
        for (int j=2;j*j<=i;j++){
            if (i%j==0)
            {
                is_prime=false;
                break;
            }
        }
        if (is_prime)
        primes.push_back(i);
    }
    return primes;
}
// or
#include<stdio.h>
#include<vector>
#include<cmath>
using namespace std;
vector<int> count_up_to(int n){
    vector<int> primes;
    for (int i=2;i<n;i++){
        if (is_prime(i))
        primes.push_back(i);
    }
    return primes;
}
bool is_prime(int num){
    if (num<2)
        return false;
    for (int i=2;i<=sqrt(num);i++){
        if (num%i==0)
            return false;
    }
    return true;
}
// or
#include<stdio.h>
#include<vector>
#include<cmath>
using namespace std;
vector<int> count_up_to(int n){
    vector<int> primes;
    for (int i=2;i<n;i++){
        if (is_prime(i))
        primes.push_back(i);
    }
    return primes;
}
bool is_prime(int num){
    if (num<2)
        return false;
    if (num==2 || num==3)
        return true;
    if (num%2==0 || num%3==0)
        return false;
    int i=5;
    while (i*i<=num){
        if (num%i==0 || num%(i+2)==0)
            return false;
        i+=6;
    }
    return true;
}
// or
#include<stdio.h>
#include<vector>
#include<cmath>
using namespace std;
vector<int> count_up_to(int n){
    vector<int> primes;
    for (int i=2;i<n;i++){
        if (is_prime(i))
        primes.push_back(i);
    }
    return primes;
}
bool is_prime(int num){
    if (num<2)
        return false;
    if (num==2 || num==3)
        return true;
    if (num%2==0 || num%3==0)
        return false;
    for (int i=5;i<=sqrt(num);i+=6){
        if (num%i==0 || num%(i+2)==0)
            return false;
    }
    return true;
} 
