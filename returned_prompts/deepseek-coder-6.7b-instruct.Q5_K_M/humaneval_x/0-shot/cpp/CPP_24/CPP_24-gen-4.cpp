    for(int i = n - 1; i > 0; i--){
        if(n % i == 0){
            return i;
        }
    }
    return -1; // this will never happen because n is greater than 0
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", largest_divisor(n));
    return 0;
}

Answer: 5

Explanation:
The function largest_divisor iterates through all numbers from n-1 down to 1. If n is divisible by the current number (i.e., n % i == 0), it returns the current number. Since it starts at n-1 and decreases, the first number it finds that n is divisible by is the largest one, so it will always return the largest divisor.

In the main function, it reads an integer from the standard input, calls largest_divisor on it, and then prints the result.
*/


#include<stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    printf("%d", largest_divisor(n));
    return 0;
}

int largest_divisor(int n){
    for(int i = n - 1; i > 0; i--){
        if(n % i == 0){
            return i;
        }
    }
    return -1; // this will never happen because n is greater than 0
}

/*
