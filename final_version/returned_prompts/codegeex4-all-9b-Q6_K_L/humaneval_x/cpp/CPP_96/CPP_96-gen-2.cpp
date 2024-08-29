```cpp
#include <vector>
#include <cmath>

using namespace std;

vector<int> count_up_to(int n) {
    vector<int> result;
    if (n <= 1) return result;

    // Create a boolean array "prime[0..n]" and initialize
    // all entries it as true. A value in prime[i] will
    // finally be false if i is Not a prime, else true bool prime[n+1];
    bool prime[n+1];
    for (int i = 2; i <= n; i++)
        prime[i] = true;

    // Mark all the multiples of prime[0] and prime[1] as false
    for (int p = 2; p <= sqrt(n); p++) {
        // If prime[p] is not changed, then it is a prime
        if (prime[p] == true) {
            // Update all multiples of p
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }

    // Collect all prime numbers less than n
    for (int p = 2; p < n; p++) {
        if (prime[p]) result.push_back(p);
    }

    return result;
}
```

这个代码实现了埃拉托色尼筛法（Sieve of Eratosthenes）来找出小于 `n` 的所有质数，并将它们存储在向量中。埃拉托色尼筛法是一种高效的算法，用于找出小于给定数的所有质数。这个算法的基本思想是从最小的质数开始，标记所有它的倍数为非质数，然后继续下一个未标记的数，重复这个过程，直到达到 `n`。最后，所有未被标记的数即为质数。