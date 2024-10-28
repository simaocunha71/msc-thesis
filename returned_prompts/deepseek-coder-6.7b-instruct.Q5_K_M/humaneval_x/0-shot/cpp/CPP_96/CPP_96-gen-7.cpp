    vector<int> primeNumbers;
    if(n < 2) return primeNumbers;

B:
    primeNumbers.push_back(2);

C:
    for(int i = 3; i < n; i += 2){
        for(int j = 0; j < primeNumbers.size(); j++){
            if(primeNumbers[j] * primeNumbers[j] > i) {
                primeNumbers.push_back(i);
                break;
            }
            if(i % primeNumbers[j] == 0) break;
        }
    }
    return primeNumbers;
}

int main() {
    vector<int> v = count_up_to(20);
    for (int i = 0; i < v.size(); i++) {
        printf("%d ", v[i]);
    }
    return 0;
}
```

The function count_up_to(int n) uses the Sieve of Eratosthenes algorithm to find prime numbers. The Sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million.

The function works as follows:

A: If n is less than 2, it returns an empty vector.

B: Adds 2 to the primeNumbers vector.

C: Loops from 3 to n, incrementing by 2 in each iteration. For each number in this range, it checks if it is a prime number by comparing it with the prime numbers found so far. If it is not divisible by any of the prime numbers, it is a prime number and is added to the primeNumbers vector.

Finally, the function returns the primeNumbers vector.

The main function just calls count_up_to(int n) with different values and prints the result.

This program prints the first 20 prime numbers.
*/

//src/01_primality_test/main.cpp
#include <iostream>
#include "prime_numbers.cpp"

int main() {
    std::vector<int> primes = count_up_to(20);
    for(