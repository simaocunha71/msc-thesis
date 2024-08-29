```cpp
#include <iostream>
#include <string>
using namespace std;

string decimal_to_binary(int decimal) {
    string binary = "db";
    while (decimal > 0) {
        binary += (decimal % 2 == 0) ? '0' : '1';
        decimal /= 2;
    }
    reverse(binary.begin() + 2, binary.end());
    binary += "db";
    return binary;
}

int main() {
    cout << decimal_to_binary(15) << endl; // returns "db1111db"
    cout << decimal_to_binary(32) << endl; // returns "db100000db"
    return 0;
}
```

This function takes an integer as input and converts it to its binary representation. The binary representation is stored in a string, starting with the characters "db". The function then returns this string.

The function uses a while loop to repeatedly divide the input number by 2 and append the remainder to the binary string. After the loop, the binary string is reversed to get the correct order of binary digits, and the characters "db" are appended to the end of the string.