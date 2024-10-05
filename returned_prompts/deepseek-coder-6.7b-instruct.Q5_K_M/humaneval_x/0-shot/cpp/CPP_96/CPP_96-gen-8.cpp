    vector<int> primes;
    if(n<2){
        return primes;
    }
    primes.push_back(2);
    for(int i=3; i<n; i+=2){
        bool is_prime = true;
        for(int j=0; j<primes.size(); j++){
            if(i%primes[j]==0){
                is_prime = false;
                break;
            }
            if(primes[j]*primes[j]>i){
                break;
            }
        }
        if(is_prime){
            primes.push_back(i);
        }
    }
    return primes;
}

// Test the function
int main() {
    int n = 18;
    vector<int> primes = count_up_to(n);
    printf("Prime numbers up to %d: ", n);
    for(int i=0; i<primes.size(); i++){
        printf("%d ", primes[i]);
    }
    printf("\n");
    return 0;
}

The function count_up_to() is implemented to find and return all the prime numbers less than n. The function uses a simple method to check if a number is prime or not. It checks if the number is divisible by any of the prime numbers less than its square root. If it is not divisible by any of them, it is a prime number.

The function first adds 2 to the list of primes (since 2 is the first prime number) and then checks the odd numbers (from 3 onwards) for primality. It uses a loop to check for divisibility and a break statement to skip the remaining iterations if the number is found to be divisible. If the number is not divisible by any of the prime numbers, it is added to the list of primes.

The function then returns the list of prime numbers.

In the main() function, the function is tested with the input 18. The prime numbers less than 18 are printed.
*/

// C++ program to find the prime numbers less than n

#include <bits/stdc++.h>