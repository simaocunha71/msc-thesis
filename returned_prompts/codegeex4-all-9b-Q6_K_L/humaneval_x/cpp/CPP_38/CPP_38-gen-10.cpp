```cpp
#include <iostream>
#include <string>

using namespace std;

string encode_cyclic(string s) {
    int l = s.length();
    int num = (l + 2) / 3;
    string x, output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x.substr(2) + x.substr(0, 2);
        output += x;
    }
    return output;
}

string decode_cyclic(string s) {
    int l = s.length();
    int num = (l + 2) / 3;
    string x, output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x.substr(2) + x.substr(0, 2);
        output += x;
    }
    return output;
}

int main() {
    string s = "HelloWorld";
    string encoded = encode_cyclic(s);
    string decoded = decode_cyclic(encoded);
    cout << "Original: " << s << endl;
    cout << "Encoded: " << encoded << endl;
    cout << "Decoded: " << decoded << endl;
    return 0;
}
```