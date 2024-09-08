    if(n<=1)
        return false;
    for(int i = 2; i*i <= n; i++)
        if(n%i == 0)
            return false;
    return true;
}

int main() {
    printf("%d\n",is_prime(6));
    printf("%d\n",is_prime(101));
    printf("%d\n",is_prime(11));
    printf("%d\n",is_prime(13441));
    printf("%d\n",is_prime(61));
    printf("%d\n",is_prime(4));
    printf("%d\n",is_prime(1));
    return 0;
}
// Correctness: 
// Time Complexity: O(sqrt(n))
// Space Complexity: O(1)


In this code, the function is_prime(n) checks whether a given number n is prime or not. It returns true if n is prime and false otherwise. The main function tests this function with different inputs. 

The function works by checking if n is less than or equal to 1, in which case it is not prime. Then it checks if n has any divisors other than 1 and itself by iterating from 2 to the square root of n. If it finds any divisor, it returns false, indicating that n is not prime. If it doesn't find any divisors, it returns true, indicating that n is prime.

The time complexity of this function is O(sqrt(n)) because it iterates up to the square root of n. The space complexity is O(1) because it uses a constant amount of space to store the variables. 

This function works correctly for all positive integers n. However, it may not work correctly for very large numbers due to the limitations of the data types used in the code. The largest number that can be represented using a long long int in C++ is 2^63-1. If you need to check prime numbers larger than this, you would need to use a library that supports arbitrary-precision arithmetic.  */



C:
#include <stdio.h>

int is_prime(int n) {
    if(n <= 1) {
        return 0;
    }
    for(int i = 2; i * i <= n; i++) {
        if(n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    printf("%d\n", is_prime(6));
    printf("%d\n", is_prime(101));
    printf("%d