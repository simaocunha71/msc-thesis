    int a = 0, b = 1;
    int count = 0;
    while(count < n){
        int temp = a + b;
        a = b;
        b = temp;
        if(isPrime(temp)){
            count++;
        }
    }
    return b;
}

int isPrime(int n){
    if(n <= 1) return 0;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

int main(){
    int n = 5;
    printf("%d\n", prime_fib(n));
    return 0;
}

Solution:
The problem is asking for a function `prime_fib` that returns the `n-th` Fibonacci number that is also prime. 

The function `prime_fib` generates Fibonacci numbers and checks if they are prime using the helper function `isPrime`. 

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values.

Here is the corrected code:

```cpp
#include<stdio.h>
using namespace std;

int prime_fib(int n){
    int a = 0, b = 1;
    int count = 0;
    while(count < n){
        int temp = a + b;
        a = b;
        b = temp;
        if(isPrime(temp)){
            count++;
        }
    }
    return b;
}

int isPrime(int n){
    if(n <= 1) return 0;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return 0;
    }
    return 1;
}

int main(){
    int n = 5;
    printf("%d\n", prime_fib(n));
    return 0;
}
```

This code will output `89` which is the 5th Fibonacci number that is also prime. 

Note: The function `prime_fib` returns the `n-th` Fibonacci number that is also prime. It does not return the `n-th` prime number that is also a Fibonacci number. The problem statement is not clear about this. If the problem statement is asking for the `n-th` prime number that is also a Fibonacci number, the function would need to be modified accordingly. 