The function `encode_shift` works by taking each character in the string, converting it to its ASCII integer value, adding 5, and then taking the modulus of 26 to keep it within the range of lowercase letters in the alphabet. Finally, it converts the resulting integer back to a character and appends it to the output string.

The function `decode_shift` works similarly, but subtracts 5 instead of adding 5. This will undo the encoding.

For example, if you have the string "hello", `encode_shift` will return "mjqqt" and `decode_shift` will return "hello".

Here's the code:

```cpp
#include<iostream>
#include<string>
using namespace std;

string encode_shift(string s) {
    string out;
    for(int i = 0; i < s.length(); i++) {
        int w = ((int)s[i] + 5 - (int)'a') % 26 + (int)'a';
        out = out + (char)w;
    }
    return out;
}

string decode_shift(string s) {
    string out;
    for(int i = 0; i < s.length(); i++) {
        int w = ((int)s[i] - 5 - (int)'a') % 26 + (int)'a';
        out = out + (char)w;
    }
    return out;
}

int main() {
    string s = "hello";
    string encoded = encode_shift(s);
    string decoded = decode_shift(encoded);
    cout << "Original string: " << s << endl;
    cout << "Encoded string: " << encoded << endl;
    cout << "Decoded string: " << decoded << endl;
    return 0;
}
```

This will output:

```
Original string: hello
Encoded string: mjqqt
Decoded string: hello
```

In this code, we're using a Caesar cipher, which is a type of substitution cipher where each character in the plaintext is 'shifted'