Here is the corrected code:

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
    for (i = 0; i < num; i++) {
        // cycle elements in each group. Unless group has fewer elements than 3.
        string x = s.substr(i * 3, 3);
        if (x.length() == 2) x = x + "a";
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

In the decode_cyclic function, we need to add a character 'a' to the end of the string if the length of the string is less than 3. This is because the encode_cyclic function moves the first character to the end of the group if the group has fewer elements than 3. We need to do the opposite in the decode_cyclic function. We also need to adjust the loop condition in the decode_cyclic function to `i < num` instead of `i * 3 < l`. This is because we need to iterate over the number of groups, not the length of the string.