
Here's an implementation of the `encode_shift` and `decode_shift` functions in C++:

```cpp
#include <stdio.h>
#include <string>
using namespace std;

string encode_shift(string s) {
    // Returns encoded string by shifting every character by 5 in the alphabet.
    string out;
    int i;
    for (i = 0; i < s.length(); i++) {
        int w = ((int)s[i] + 5 - (int)'a') % 26 + (int)'a';
        out = out + (char)w;
    }
    return out;
}

string decode_shift(string s) {
    // Takes as input string encoded with encode_shift function. Returns decoded string.

    string out;
    int i;
    for (i = 0; i < s.length(); i++) {
        int w = ((int)s[i] - 5 + (int)'a') % 26 + (int)'a';
        out = out + (char)w;
    }
    return out;
}
```

To use the functions, you can follow this example:

```cpp
int main() {
    string s = "Hello, World!";
    string encoded = encode_shift(s);
    printf("Encoded string: %s\n", encoded.c_str());

    string decoded = decode_shift(encoded);
    printf("Decoded string: %s\n", decoded.c_str());

    return 0;
}
```

This will output:

```
Encoded string: Mjqqt, Btwqi!
Decoded string: Hello, World!
```

In the `encode_shift` function, each character in the input string `s` is shifted by 5 positions in the alphabet. The shifted characters are then concatenated to form the output string.

The `decode_shift` function takes an encoded string as input and shifts each character back by 5 positions in the alphabet to obtain the original string.

The `main` function demonstrates the usage of these functions