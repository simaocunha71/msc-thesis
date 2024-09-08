    vector<int> factors;
    for(int i = 2; i <= n; i++){
        int count = 0;
        while(n % i == 0){
            n /= i;
            count++;
        }
        if(count > 0){
            factors.push_back(i);
            factors.insert(factors.end(), count, i);
        }
    }
    if(n > 1) factors.push_back(n);
    return factors;
} // Return vector of prime factors of given integer in the order from smallest to largest.
// Each of the factors should be vectored number of times corresponding to how many times it appeares in factorization.
// Input number should be equal to the product of all factors
int main() {
    printf("%d\n", sizeof(int));
    printf("%d\n", sizeof(vector<int>));
    printf("%d\n", sizeof(vector<int>()));
    vector<int> factors = factorize(8);
    for(auto f: factors) printf("%d ", f);
    printf("\n");
    factors = factorize(25);
    for(auto f: factors) printf("%d ", f);
    printf("\n");
    factors = factorize(70);
    for(auto f: factors) printf("%d ", f);
    printf("\n");
    return 0;
}

R:
Here is the solution in C++:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> factorize(int n) {
    std::vector<int> factors;
    for (int i = 2; i * i <= n; i++) {
        int count = 0;
        while (n % i == 0) {
            n /= i;
            count++;
        }
        if (count > 0) {
            factors.push_back(i);
            factors.insert(factors.end(), count, i);
        }
    }
    if (n > 1) {
        factors.push_back(n);
    }
    std::sort(factors.begin(), factors.end());
    return factors;
}

int main() {
    std::vector<int> factors = factorize(8);
    for (auto f : factors) {
        std::cout << f << " ";
    }
    std::cout << std::endl;
    factors = factorize(25);
    for (auto f : factors) {
        std::cout << f << " ";
    }
    std::cout << std::endl;
    factors = factorize(70);
   