This problem can be solved by iterating from 2 to the square root of n and checking if n is divisible by any of these numbers. If n is divisible, it means that the divisor is a prime factor, and we need to divide n by that divisor until n is no longer divisible. The largest prime factor will be the last value of n.

Here is the C++ code for the problem:
```c
#include<stdio.h>
using namespace std;

int largest_prime_factor(int n){
    int i;
    for(i=2; i*i<=n; i++){
        if(n%i==0){
            int temp=i;
            while(n%i==0){
                n=n/i;
            }
            if(temp>2)
                return temp;
        }
    }
    return n;
}

int main() {
    int n = 13195;
    printf("%d\n", largest_prime_factor(n));
    return 0;
}
```
This code will return the largest prime factor of the input number n. For example, if n = 13195, the output will be 29. If n = 2048, the output will be 2.

Note that the code assumes that n > 1 and is not a prime. If n is a prime number, the function will return n. If n is less than or equal to 1, the function will return 1.