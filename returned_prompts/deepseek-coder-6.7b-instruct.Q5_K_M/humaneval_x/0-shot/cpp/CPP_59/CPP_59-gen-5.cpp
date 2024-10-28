    int largest_factor = 2;
    while (n % 2 == 0) {
        n = n / 2;
    }
    for (int i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            largest_factor = i;
            n = n / i;
        }
    }
    if (n > 2) {
        largest_factor = n;
    }
    return largest_factor;
}

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    printf("Largest prime factor: %d\n", largest_prime_factor(number));
    return 0;
}
*/

//Program to find the largest prime factor of a number
#include <stdio.h>
#include <math.h>

int largest_prime_factor(int n){
    int largest_factor = 2;
    while (n % 2 == 0) {
        n = n / 2;
    }
    for (int i = 3; i <= sqrt(n); i += 2) {
        while (n % i == 0) {
            largest_factor = i;
            n = n / i;
        }
    }
    if (n > 2) {
        largest_factor = n;
    }
    return largest_factor;
}

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    printf("Largest prime factor: %d\n", largest_prime_factor(number));
    return 0;
}