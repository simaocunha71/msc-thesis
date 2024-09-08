```cpp
#include <iostream>
#include <string>
using namespace std;

string encode_shift(string s) {
    // returns encoded string by shifting every character by 5 in the alphabet.
    string out;
    int i;
    for (i = 0; i < s.length(); i++) {
        int w = ((int)s[i] + 5 - (int)'a') % 26 + (int)'a';
        out = out + (char)w;
    }
    return out;
}

string decode_shift(string s) {
    // takes as input string encoded with encode_shift function. Returns decoded string.
    string out;
    int i;
    for (i = 0; i < s.length(); i++) {
        int w = ((int)s[i] - 5 - (int)'a') % 26 + (int)'a';
        out = out + (char)w;
    }
    return out;
}

int main() {
    string test = "hello";
    string encoded = encode_shift(test);
    string decoded = decode_shift(encoded);
    cout << "Original: " << test << endl;
    cout << "Encoded: " << encoded << endl;
    cout << "Decoded: " << decoded << endl;
    return 0;
}
```

This program defines two functions, `encode_shift` and `decode_shift`, which encode and decode a string by shifting each character by 5 positions in the alphabet. The `main` function tests these functions by encoding a string, decoding the encoded string, and printing the results.