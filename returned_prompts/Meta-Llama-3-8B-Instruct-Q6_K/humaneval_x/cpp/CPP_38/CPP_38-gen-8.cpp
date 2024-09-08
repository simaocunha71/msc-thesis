Here is the correct implementation of the encode_cyclic and decode_cyclic functions in C++:

```cpp
#include <iostream>
#include <string>
using namespace std;

string encode_cyclic(string s) {
    // returns encoded string by cycling groups of three characters.  
    // split string to groups. Each of length 3.
    int l = s.length();
    int num = (l + 2) / 3;
    string x, output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        // cycle elements in each group. Unless group has fewer elements than 3.
        x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x.substr(1) + x[0];
        output = output + x;
    }
    return output;
}

string decode_cyclic(string s) {
    // takes as input string encoded with encode_cyclic function. Returns decoded string. 
    string output, temp;
    int i = 0;
    while (i < s.length()) {
        temp = "";
        if (i + 2 < s.length()) {
            temp = s.substr(i, 2) + s[i];
        } else {
            temp = s.substr(i);
        }
        output = output + temp;
        i += 3;
    }
    return output;
}

int main() {
    string s = "Hello, World!";
    string encoded = encode_cyclic(s);
    string decoded = decode_cyclic(encoded);
    cout << "Encoded: " << encoded << endl;
    cout << "Decoded: " << decoded << endl;
    return 0;
}
```

In the `encode_cyclic` function, we iterate over the input string in groups of 3 characters. If a group has 3 characters, we cycle the first and second characters. We then concatenate the encoded groups to form the output string.

In the `decode_cyclic` function, we iterate over the input string in groups of 3 characters. We decode each group by taking the last character of the group and prepending it to the first two characters. We then concatenate the decoded groups to form the output string. If the last group has fewer than 3 characters, we simply append the remaining characters to the output string.

The `main` function demonstrates the usage of the `encode_cyclic` and `decode_cyclic` functions. It encodes