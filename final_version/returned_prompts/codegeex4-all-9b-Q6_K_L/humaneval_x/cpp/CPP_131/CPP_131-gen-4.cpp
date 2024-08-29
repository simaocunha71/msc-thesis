#include <iostream>
using namespace std;

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    bool hasOddDigit = false;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
            hasOddDigit = true;
        }
    }
    return hasOddDigit ? product : 0;
}

int main() {
    cout << digits(235) << endl;  // Output: 15
    return 0;
}
B:
#include <iostream>
using namespace std;

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 == 0) {
            return 0;
        } else {
            product *= digit;
        }
    }
    return product;
}

int main() {
    cout << digits(235) << endl;  // Output: 15
    return 0;
}
C:
#include <iostream>
using namespace std;

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    return product;
}

int main() {
    cout << digits(235) << endl;  // Output: 15
    return 0;
}
D:
#include <iostream>
using namespace std;

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 == 0) {
            product = 0;
            break;
        } else {
            product *= digit;
        }
    }
    return product;
}

int main() {
    cout << digits(235) << endl;  // Output: 15
    return 0;
}
E:
#include <iostream>
using namespace std;

int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (char c : s) {
        int digit = c - '0';
        if (digit % 2 == 0) {
           