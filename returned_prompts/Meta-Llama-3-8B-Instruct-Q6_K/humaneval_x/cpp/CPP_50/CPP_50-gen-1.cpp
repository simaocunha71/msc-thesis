Here is the correct code:

```cpp
#include <iostream>
#include <string>
using namespace std;

string encode_shift(string s) {
    // returns encoded string by shifting every character by 5 in the alphabet.
    string out;
    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i])) {
            char c = s[i];
            if (islower(c)) {
                c = 'a' + (c - 'a' + 5) % 26;
            } else {
                c = 'A' + (c - 'A' + 5) % 26;
            }
            out += c;
        } else {
            out += s[i];
        }
    }
    return out;
}

string decode_shift(string s) {
    // takes as input string encoded with encode_shift function. Returns decoded string.
    string out;
    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i])) {
            char c = s[i];
            if (islower(c)) {
                c = 'a' + (c - 'a' - 5 + 26) % 26;
            } else {
                c = 'A' + (c - 'A' - 5 + 26) % 26;
            }
            out += c;
        } else {
            out += s[i];
        }
    }
    return out;
}

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    string encoded = encode_shift(str);
    cout << "Encoded string: " << encoded << endl;
    string decoded = decode_shift(encoded);
    cout << "Decoded string: " << decoded << endl;
    return 0;
}
```

This code will encode and decode the input string by shifting every alphabetic character by 5 positions in the alphabet. Non-alphabetic characters will be left unchanged. The encoded and decoded strings will be printed out. 

The `encode_shift` function shifts each alphabetic character by 5 positions in the alphabet. If the character is lowercase, it is shifted from 'a' to 'z', wrapping around from 'z' to 'a' if necessary. If the character is uppercase, it is shifted from 'A' to 'Z', wrapping around from 'Z' to 'A' if necessary. Non-alphabetic characters are left unchanged