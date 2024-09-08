Here is the code:

```cpp
#include <iostream>

using namespace std;

int sum_to_n(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

int main() {
    int n;
    cout << "Enter the number: ";
    cin >> n;
    cout << "The sum of numbers from 1 to " << n << " is " << sum_to_n(n) << endl;
    return 0;
}
```

This program calculates the sum of all numbers from 1 to n, where n is the input provided by the user. The function `sum_to_n(int n)` calculates this sum using a for loop, and the main function prompts the user to input a number and then prints the sum of all numbers from 1 to that number.