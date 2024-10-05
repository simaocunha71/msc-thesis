    if(n < 0){
        return -1;
    }
    if(n == 1){
        return 2;
    }
    return 2 * starts_one_ends(n-1);
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", starts_one_ends(n));
    return 0;
}
*/

/*
The function starts_one_ends(n) calculates the count of n-digit positive integers that start or end with 1. This can be calculated by a simple mathematical formula: 2^(n-1). This formula is based on the fact that for each n-digit number that starts or ends with 1, there are two possible n-1 digit numbers that can follow.

If n is 1, the function returns 2 because there are two single-digit numbers that start or end with 1 (1 and 1). If n is less than 1, the function returns -1 because a positive integer cannot have a negative number of digits.
*/

#include<stdio.h>

int starts_one_ends(int n){
    if(n < 1){
        return -1;
    }
    if(n == 1){
        return 2;
    }
    return 2 * starts_one_ends(n-1);
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", starts_one_ends(n));
    return 0;
}

//src/recursion/starts_one_ends.c
#include <stdio.h>

int starts_one_ends(int n) {
    if (n < 1) {
        return -1;
    }
    if (n == 1) {
        return 2;
    }
    return 2 * starts_one_ends(n-1);
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", starts_one_ends(n));
    return 0;
}

//src/recursion/