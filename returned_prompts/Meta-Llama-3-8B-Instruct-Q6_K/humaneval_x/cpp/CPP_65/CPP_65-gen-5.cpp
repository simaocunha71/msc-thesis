    // Calculate the number of digits in the integer
    int num_digits = 0;
    int temp = x;
    while(temp != 0) {
        temp /= 10;
        num_digits++;
    }

    // Calculate the actual shift
    shift = shift % num_digits;

    // Split the digits into an array
    int digits[num_digits];
    temp = x;
    for(int i = 0; i < num_digits; i++) {
        digits[i] = temp % 10;
        temp /= 10;
    }

    // Perform the circular shift
    for(int i = 0; i < shift; i++) {
        int last_digit = digits[num_digits - 1];
        for(int j = num_digits - 1; j > 0; j--) {
            digits[j] = digits[j - 1];
        }
        digits[0] = last_digit;
    }

    // Convert the array back to a string
    string result = "";
    for(int i = 0; i < num_digits; i++) {
        result += to_string(digits[i]);
    }

    return result;
}

C++:
```c
#include <iostream>
#include <string>
using namespace std;

string circularShift(int x, int shift) {
    string s = to_string(x);
    int n = s.length();
    shift = shift % n;
    if (shift == 0) {
        return s;
    }
    string left = s.substr(shift);
    string right = s.substr(0, shift);
    return left + right;
}

int main() {
    cout << circularShift(12, 1) << endl;  // Output: 21
    cout << circularShift(12, 2) << endl;  // Output: 12
    return 0;
}
```
The code converts the integer into a string, calculates the actual shift by taking the modulus of the shift with the number of digits, and then performs the circular shift by concatenating the right part of the string with the left part. If the shift is 0, it returns the original string.