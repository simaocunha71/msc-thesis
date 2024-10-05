    vector<int> factors;
    for(int i = 2; i*i <= n; i++){
        while(n % i == 0){
            factors.push_back(i);
            n /= i;
        }
    }
    if(n != 1)
        factors.push_back(n);
    return factors;
}
int main(){
    int n;
    scanf("%d",&n);
    vector<int> res = factorize(n);
    for(int i = 0; i < res.size(); i++)
        printf("%d ",res[i]);
    return 0;
}
*/

#include <iostream>
#include <vector>
using namespace std;

// Function to check if a number is prime
bool isPrime(int n){
    if(n <= 1)
        return false;
    if(n <= 3)
        return true;
    if(n % 2 == 0 || n % 3 == 0)
        return false;
    for(int i = 5; i*i <= n; i += 6)
        if(n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

// Function to find all prime factors of a number
vector<int> findPrimeFactors(int n){
    vector<int> primeFactors;
    // Find divisors of 2
    while(n % 2 == 0){
        primeFactors.push_back(2);
        n = n / 2;
    }
    // Find odd divisors
    for(int i = 3; i <= sqrt(n); i += 2){
        while(n % i == 0){
            primeFactors.push_back(i);
            n = n / i;
        }
    }
    // If n is a prime number and n is greater than 2
    if(n > 2)
        primeFactors.push_back(n);
    return primeFactors;
}

int main(){
    int n;
    cin >> n;
    vector<int> primeFactors = findPr