    for(int i = n-1; i > 1; i--){
        if(n%i == 0){
            return i;
        }
    }
    return 1;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Largest divisor: %d\n", largest_divisor(n));
    return 0;
}

R:
```c
#include<stdio.h>
using namespace std;

int largest_divisor(int n){
    for(int i = n-1; i > 1; i--){
        if(n%i == 0){
            return i;
        }
    }
    return 1;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Largest divisor: %d\n", largest_divisor(n));
    return 0;
}
```



This C++ program takes an integer as input from the user and prints the largest divisor of the number. The function `largest_divisor` iterates from `n-1` to `2` and checks if the current number is a divisor of `n`. If it is, the function returns that number. If no divisors are found, the function returns `1` (since `1` is a divisor of every number). The `main` function takes the input from the user, calls the `largest_divisor` function, and prints the result. 

For example, if the input is `15`, the program will print `5` as the largest divisor of `15`. 

Note: The function `largest_divisor` does not handle the case where `n` is `1`, since `1` is not considered a divisor of itself in this context. If you need to handle this case, you can add a check at the beginning of the function. 

Also, the function `largest_divisor` is not very efficient for large values of `n`, since it checks all numbers from `n-1` to `2`. A more efficient approach would be to check divisibility up to the square root of `n`, since a larger factor of `n` would be a multiple of a smaller factor that has already been checked. 

Here is an updated version of the function that uses this approach:

```c
int largest_divisor(int n){
    for(int i = n/2; i > 1; i--){
        if(n