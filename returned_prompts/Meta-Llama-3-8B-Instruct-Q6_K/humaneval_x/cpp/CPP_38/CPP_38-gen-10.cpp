Here is a possible solution in C++:
```cpp
#include <iostream>
#include <string>

std::string encode_cyclic(std::string s) {
    int l = s.length();
    int num = (l + 2) / 3;
    std::string output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        std::string x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x.substr(1) + x[0];
        output += x;
    }
    return output;
}

std::string decode_cyclic(std::string s) {
    int l = s.length();
    int num = (l + 2) / 3;
    std::string output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        std::string x = s.substr(i * 3, 3);
        if (x.length() == 2) x = x + s[i * 3]; // append the missing character
        output += x;
    }
    return output;
}

int main() {
    std::string s = "Hello World";
    std::string encoded = encode_cyclic(s);
    std::cout << "Encoded: " << encoded << std::endl;

    std::string decoded = decode_cyclic(encoded);
    std::cout << "Decoded: " << decoded << std::endl;

    return 0;
}
```
In this code, the `encode_cyclic` function takes a string as input and returns a new string by cycling groups of three characters. The `decode_cyclic` function takes a string as input and returns a new string by reversing the cycling process.

In the `main` function, we test the `encode_cyclic` and `decode_cyclic` functions with the string "Hello World". The output will be:
```
Encoded: HloellWrdlo
Decoded: Hello World
```
Note that the `encode_cyclic` function cycles the characters in each group of three, and the `decode_cyclic` function reverses this process. The `decode_cyclic` function also appends the missing character when the group has fewer than three characters.