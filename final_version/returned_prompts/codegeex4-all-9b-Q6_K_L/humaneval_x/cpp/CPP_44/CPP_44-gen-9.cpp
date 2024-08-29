#include <iostream>
#include <string>

using namespace std;

string change_base(int x, int base) {
    string result = "";
    while (x > 0) {
        int remainder = x % base;
        result = to_string(remainder) + result;
        x /= base;
    }
    return result;
}

int main() {
    cout << change_base(8, 3) << endl;  // Output: "22"
    cout << change_base(8, 2) << endl;  // Output: "1000"
    cout << change_base(7, 2) << endl;  // Output: "111"
    return 0;
}

B:
#include <iostream>
#include <string>
using namespace std;
string change_base(int x, int base) {
    string result = "";
    while (x > 0) {
        int remainder = x % base;
        result = to_string(remainder) + result;
        x /= base;
    }
    return result;
}
C:
#include <iostream>
#include <string>
using namespace std;
string change_base(int x, int base) {
    string result = "";
    while (x > 0) {
        int remainder = x % base;
        result = to_string(remainder) + result;
        x /= base;
    }
    return result;
}

int main() {
    cout << change_base(8, 3) << endl;  // Output: "22"
    cout << change_base(8, 2) << endl;  // Output: "1000"
    cout << change_base(7, 2) << endl;  // Output: "111"
    return 0;
}

D:
#include <iostream>
#include <string>
using namespace std;
string change_base(int x, int base) {
    string result = "";
    while (x > 0) {
        int remainder = x % base;
        result = to_string(remainder) + result;
        x /= base;
    }
    return result;
}

int main() {
    cout << change_base(8, 3) << endl;  // Output: "22"
    cout << change_base(8, 2) << endl;  // Output: "1000"
    cout << change_base(7, 2) << endl;  // Output: "111"
    return 0;
}

E:
#include <iostream>
#include <string>
using namespace std;
string change