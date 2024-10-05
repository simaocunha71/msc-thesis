    int count = 0;
    for(int i = 2; i <= a/2; i++){
        if(a % i == 0){
            if(i % 2 != 0){
                count++;
            }
        }
    }
    if(count == 3){
        return true;
    }
    else{
        return false;
    }
}

int main()
{
    printf("%d\n", is_multiply_prime(30));
    return 0;
}


A: It's not right to assume that a number is a multiplication of 3 prime numbers if it's divisible by 2 prime numbers. The number 30, for example, is divisible by 2 prime numbers 2 and 5, so it's not a multiplication of 3 primes.

Here's the correct code:

#include <iostream>
#include <vector>
using namespace std;

vector<int> prime_factors(int a) {
    vector<int> factors;
    for (int i = 2; a > 1; i++) {
        while (a % i == 0) {
            factors.push_back(i);
            a /= i;
        }
    }
    return factors;
}

bool is_multiply_prime(int a){
    vector<int> factors = prime_factors(a);
    if (factors.size() == 3) {
        for (int i = 0; i < 3; i++) {
            for (int j = i+1; j < 3; j++) {
                if (factors[i] == factors[j]) return false;
            }
        }
        return true;
    }
    return false;
}

int main() {
    cout << (is_multiply_prime(30) ? "true" : "false") << endl;
    return 0;
}

This code first finds all prime factors of a number, then checks if there are exactly 3 of them. If so, it checks if they are all different. If they are, it returns true; otherwise, it returns false.