Here is the corrected version of your code:

```cpp
#include <iostream>
#include <string>
using namespace std;

string encode_cyclic(string s) {
    // returns encoded string by cycling groups of three characters.
    int l = s.length();
    int num = (l + 2) / 3;
    string output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        // cycle elements in each group. Unless group has fewer elements than 3.
        string x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x.substr(1) + x[0];
        output += x;
    }
    return output;
}

string decode_cyclic(string s) {
    // takes as input string encoded with encode_cyclic function. Returns decoded string.
    int l = s.length();
    int num = (l + 2) / 3;
    string output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        // cycle elements in each group. Unless group has fewer elements than 3.
        string x = s.substr(i * 3, 3);
        if (x.length() == 2) x = x[1] + x[0];
        output += x;
    }
    return output;
}

int main() {
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    string encoded = encode_cyclic(s);
    cout << "Encoded string: " << encoded << endl;
    string decoded = decode_cyclic(encoded);
    cout << "Decoded string: " << decoded << endl;
    return 0;
}
```

This code works by cycling groups of three characters in the input string. The encode function shifts the first character of each group to the end of the group, and the decode function shifts the first character back to the beginning of the group if the group has fewer than three characters. The main function demonstrates the use of these functions by encoding and decoding a user-input string.