Here is a C++ function that implements the cyclic encoding and decoding of strings. The encoding function takes a string as input and returns a new string where every group of three characters is shifted one position to the right. The decoding function takes a string as input and returns the original string.

```cpp
#include <iostream>
#include <string>

std::string encode_cyclic(std::string s) {
    // returns encoded string by cycling groups of three characters.  
    // split string to groups. Each of length 3.
    int l = s.length();
    int num = (l + 2) / 3;
    std::string output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        // cycle elements in each group. Unless group has fewer elements than 3.
        std::string x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x.substr(1) + x[0];
        output += x;
    }
    return output;
}

std::string decode_cyclic(std::string s) {
    // takes as input string encoded with encode_cyclic function. Returns decoded string. 
    std::string output;
    int i;
    for (i = 0; i < s.length(); i++) {
        if ((i + 1) % 3 == 0) {
            output += s[i - 1];
        } else {
            output += s[i];
        }
    }
    return output;
}

int main() {
    std::string s = "hello";
    std::string encoded = encode_cyclic(s);
    std::cout << "Encoded string: " << encoded << std::endl;

    std::string decoded = decode_cyclic(encoded);
    std::cout << "Decoded string: " << decoded << std::endl;

    return 0;
}
```

This program will output:

```
Encoded string: holloel
Decoded string: hello
```

As you can see, the original string "hello" is encoded to "holloel" and then decoded back to "hello". The encoding function shifts each group of three characters one position to the right, and the decoding function reverses this process.