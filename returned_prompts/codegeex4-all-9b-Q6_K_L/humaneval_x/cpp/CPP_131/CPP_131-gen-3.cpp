#include <iostream>
#include <string>
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
    cout << digits(1) << endl;
    cout << digits(4) << endl;
    cout << digits(235) << endl;
    return 0;
}
B:
#include <iostream>
#include <string>
using namespace std;
int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (int i = 0; i < s.length(); i++) {
        int digit = s[i] - '0';
        if (digit % 2 == 0) {
            return 0;
        } else {
            product *= digit;
        }
    }
    return product;
}
int main() {
    cout << digits(1) << endl;
    cout << digits(4) << endl;
    cout << digits(235) << endl;
    return 0;
}
C:
#include <iostream>
#include <string>
using namespace std;
int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (int i = 0; i < s.length(); i++) {
        int digit = s[i] - '0';
        if (digit % 2 != 0) {
            product *= digit;
        }
    }
    return product;
}
int main() {
    cout << digits(1) << endl;
    cout << digits(4) << endl;
    cout << digits(235) << endl;
    return 0;
}
D:
#include <iostream>
#include <string>
using namespace std;
int digits(int n) {
    string s = to_string(n);
    int product = 1;
    for (int i = 0; i < s.length(); i++) {
        int digit = s[i] - '0';
        if (digit % 2 == 1) {
            return 0;
        } else {
            product *= digit;
        }
    }
    return product;
}
int main() {
    cout << digits(1) << endl;
    cout << digits(4)