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
        primes.push_back(i);
    }
    return primes;
} // O(n^2) solution
// O(n log n) solution:
#include<vector>
#include<cmath>
using namespace std;
vector<int> count_up_to(int n)
{
    vector<bool> is_prime(n+1, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i*i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i*i; j <= n; j += i) {
                is_prime[j] = false;
            }
        }
    }
    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
        }
    }
    return primes;
} // O(n log n) solution


