    int a = 0, b = 1, count = 1;
    while(count < n){
        int c = a + b;
        if(c % 2 != 0 && c > 1){
            a = b;
            b = c;
            count++;
        }else{
            a = a + a;
            b = a + b;
        }
    }
    return b;
}

int main(){
    printf("%d\n",prime_fib(5));
    return 0;
}

Answer:
The problem with this code is that it doesn't correctly check for primality of Fibonacci numbers. The code checks for primality by checking if the number is odd and greater than 1, which is not correct. 

Here's the corrected code:

```cpp
#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int prime_fib(int n) {
    int a = 0, b = 1, count = 1;
    while (count < n) {
        int c = a + b;
        if (isPrime(c)) {
            a = b;
            b = c;
            count++;
        } else {
            a = a + a;
            b = a + b;
        }
    }
    return b;
}

int main() {
    cout << prime_fib(5) << endl;
    return 0;
}
```

In this code, we use a helper function `isPrime` to check if a number is prime. We then use this function in the `prime_fib` function to check if the Fibonacci number is prime. If it is, we increment the count and update `a` and `b`. If it's not, we update `a` and `b` without incrementing the count. This way, we correctly find the `n`-th Fibonacci number that is also prime.