Here is the C++ code for the encode_shift and decode_shift functions. These functions shift each character in the input string by 5 positions in the alphabet.

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
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    string encoded = encode_shift(s);
    string decoded = decode_shift(encoded);
    cout << "Encoded string: " << encoded << endl;
    cout << "Decoded string: " << decoded << endl;
    return 0;
}
```

This code prompts the user to enter a string, encodes it using the `encode_shift` function, decodes the encoded string using the `decode_shift` function, and then prints both the original and decoded strings. The `encode_shift` function shifts each character in the input string by 5 positions in the alphabet, wrapping around to the beginning of the alphabet if necessary. The `decode_shift` function reverses this process by shifting each character back by 5 positions. The `main` function demonstrates the use of these functions by encoding and decoding a user-input string.