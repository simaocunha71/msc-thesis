Here is the C++ code to solve the problem:
```c
#include <iostream>
using namespace std;

int largest_divisor(int n) {
    int i;
    for(i=n-1; i>0; i--){
        if(n%i==0)
            return i;
    }
    return 1;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "The largest divisor of " << n << " is " << largest_divisor(n) << endl;
    return 0;
}
```

This program takes an integer input from the user, and then calculates and prints the largest divisor of the input number. The function `largest_divisor` uses a for loop to iterate from `n-1` down to `1`, checking if each number is a divisor of `n` by using the modulus operator (`%`). If a divisor is found, the function returns that divisor. If no divisors are found, the function returns `1`, which is the smallest possible divisor. The `main` function prompts the user to enter a number, calls the `largest_divisor` function with that number, and then prints the result.