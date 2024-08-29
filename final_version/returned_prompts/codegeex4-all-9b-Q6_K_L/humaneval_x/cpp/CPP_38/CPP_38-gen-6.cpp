Here's a possible solution in C++:

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
        //cycle elements in each group. Unless group has fewer elements than 3.
        x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x.substr(1) + x[0];
        output += x;
    }
    return output;
}

string decode_cyclic(string s) {
    /*
    takes as input string encoded with encode_cyclic function. Returns decoded string. 
    */
    int l = s.length();
    int num = (l + 2) / 3;
    string x, output;
    int i;
    for (i = 0; i * 3 < l; i++) {
        //decode each group. 
        x = s.substr(i * 3, 3);
        if (x.length() == 3) x = x[x.length() - 1] + x.substr(0, x.length() - 1);
        output += x;
    }
    return output;
}

int main() {
    string s = "Hello World!";
    string encoded = encode_cyclic(s);
    string decoded = decode_cyclic(encoded);

    cout << "Original string: " << s << endl;
    cout << "Encoded string: " << encoded << endl;
    cout << "Decoded string: " << decoded << endl;

    return 0;
}
```

The `encode_cyclic` function cycles each group of three characters in the string. The `decode_cyclic` function decodes the string by reversing the process.

The `main` function demonstrates the usage of the `encode_cyclic` and `decode_cyclic` functions. It encodes a string, then decodes the encoded string, and prints all three strings to the console.