#include <iostream>
#include <string>
using namespace std;

string string_xor(string a, string b) {
    int max_length = max(a.length(), b.length());
    a = string(max_length - a.length(), '0') + a;
    b = string(max_length - b.length(), '0') + b;
    string result = "";
    for (int i = 0; i < max_length; i++) {
        if (a[i] == b[i])
            result += "0";
        else
            result += "1";
    }
    return result;
}

int main() {
    cout << string_xor("010", "110") << endl; // prints "100"
    return 0;
}

B:
#include <iostream>
#include <string>
using namespace std;

string string_xor(string a, string b) {
    int max_length = max(a.length(), b.length());
    a = string(max_length - a.length(), '0') + a;
    b = string(max_length - b.length(), '0') + b;
    string result = "";
    for (int i = 0; i < max_length; i++) {
        if (a[i] == b[i])
            result += "0";
        else
            result += "1";
    }
    return result;
}

int main() {
    cout << string_xor("010", "110") << endl; // prints "100"
    return 0;
}

C:
#include <iostream>
#include <string>
using namespace std;

string string_xor(string a, string b) {
    int max_length = max(a.length(), b.length());
    a = string(max_length - a.length(), '0') + a;
    b = string(max_length - b.length(), '0') + b;
    string result = "";
    for (int i = 0; i < max_length; i++) {
        if (a[i] == b[i])
            result += "0";
        else
            result += "1";
    }
    return result;
}

int main() {
    cout << string_xor("010", "110") << endl; // prints "100"
    return 0;
}

D:
#include <iostream>
#include <string>
using namespace std;

string string_xor(string a, string b) {
    int max_length = max(a.length(), b.length());
    a = string(max_length - a.length(), '0') + a;
    b = string(max_length - b.length