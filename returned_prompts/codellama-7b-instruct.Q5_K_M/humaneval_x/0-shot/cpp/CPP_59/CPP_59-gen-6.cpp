
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int largest_prime_factor(int n) {
    if(n == 1) return 1;
    if(n == 2) return 2;
    int i = 2;
    while(i < (int) sqrt(n)) {
        if(n % i == 0 && is_prime(i)) return i;
        i++;
    }
    return n;
}

int is_prime(int n) {
    if(n == 2) return 1;
    int i = 2;
    while(i < (int) sqrt(n)) {
        if(n % i == 0) return 0;
        i++;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", largest_prime_factor(n));
    return 0;
}




