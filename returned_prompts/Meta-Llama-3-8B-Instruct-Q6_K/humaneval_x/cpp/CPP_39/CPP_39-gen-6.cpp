Here is the correct solution:

```cpp
#include <iostream>
using namespace std;

bool is_prime(int num) {
    if(num <= 1) return false;
    for(int i = 2; i*i <= num; i++) {
        if(num%i == 0) return false;
    }
    return true;
}

int prime_fib(int n) {
    int a = 1, b = 1, count = 1;
    while(count < n) {
        int temp = a+b;
        a = b;
        b = temp;
        if(is_prime(b)) {
            count++;
        }
    }
    return b;
}

int main() {
    int n;
    cout << "Enter the number: ";
    cin >> n;
    cout << n << "th number that is a Fibonacci number and it's also prime is: " << prime_fib(n) << endl;
    return 0;
}
```

This program will calculate the nth Fibonacci number that is also prime. The function `is_prime` checks if a number is prime, and the function `prime_fib` calculates the nth Fibonacci number that is also prime. The main function asks the user for the number n and then prints the result.