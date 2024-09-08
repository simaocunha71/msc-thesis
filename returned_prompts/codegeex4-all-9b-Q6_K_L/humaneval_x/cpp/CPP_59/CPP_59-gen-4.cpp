#include <iostream>
#include <cmath>
using namespace std;

int largest_prime_factor(int n)
{
    int max_prime = -1;
    while (n % 2 == 0)
    {
        max_prime = 2;
        n >>= 1; // equivalent to n /= 2
    }
    for (int i = 3; i <= sqrt(n); i += 2)
    {
        while (n % i == 0)
        {
            max_prime = i;
            n = n / i;
        }
    }
    if (n > 2)
        max_prime = n;
    return max_prime;
}

int main()
{
    cout << largest_prime_factor(13195) << endl;
    cout << largest_prime_factor(2048) << endl;
    return 0;
}