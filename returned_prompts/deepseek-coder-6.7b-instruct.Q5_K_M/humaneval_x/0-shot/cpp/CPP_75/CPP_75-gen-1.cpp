
}
int main() {
    printf("%d", is_multiply_prime(30));
    return 0;
}

//SOLUTION:
#include<stdio.h>
bool is_prime(int n) {
    if (n<=1)
        return false;
    if (n==2)
        return true;
    if (n%2 == 0)
        return false;
    for (int i=3; i*i<=n; i+=2) {
        if(n % i == 0)
            return false;
    }
    return true;
}

bool is_multiply_prime(int a) {
    int count = 0;
    for (int i=2; i*i<=a; i++) {
        if (a % i == 0 && is_prime(i)) {
            if (a / i != i) {
                if (is_prime(a / i)) {
                    count += 2;
                } else {
                    return false;
                }
            } else {
                if (is_prime(i)) {
                    count += 1;
                } else {
                    return false;
                }
            }
        }
    }
    if (is_prime(a)) {
        count += 1;
    }
    return count == 3;
}

int main() {
    printf("%d", is_multiply_prime(30));
    return 0;
}

This function is_multiply_prime checks if the given number is the multiplication of exactly 3 prime numbers. It uses the helper function is_prime to check if a number is prime. The function is_multiply_prime iterates over all numbers from 2 to the square root of the given number and checks if the given number is divisible by the current number and if the current number is prime. If the given number is divisible by the current number, it checks if the quotient is prime. The function increments the count if the current number and the quotient are both prime. Finally, it returns true if the count is 3 and false otherwise.

Please, note that the function is_multiply_prime