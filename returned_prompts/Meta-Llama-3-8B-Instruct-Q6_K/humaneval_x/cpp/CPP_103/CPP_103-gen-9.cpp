Here is the C++ code that solves the problem:
```cpp
#include <iostream>
#include <string>
using namespace std;

string rounded_avg(int n, int m) {
    if (n > m) {
        return "-1";
    }
    int sum = 0;
    int count = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
        count++;
    }
    double avg = sum / (double)count;
    int rounded_avg = (int)round(avg);
    string result = "";
    while (rounded_avg > 0) {
        result = (char)('0' + rounded_avg % 2) + result;
        rounded_avg /= 2;
    }
    return result;
}

int main() {
    cout << rounded_avg(1, 5) << endl;
    cout << rounded_avg(7, 5) << endl;
    cout << rounded_avg(10, 20) << endl;
    cout << rounded_avg(20, 33) << endl;
    return 0;
}
```
This code defines a function `rounded_avg` that takes two integer arguments `n` and `m`, and returns a string representing the binary representation of the rounded average of the integers from `n` to `m`.

The function first checks if `n` is greater than `m`, and returns "-1" if so. Otherwise, it calculates the sum of the integers from `n` to `m`, and then calculates the average by dividing the sum by the count of integers.

The average