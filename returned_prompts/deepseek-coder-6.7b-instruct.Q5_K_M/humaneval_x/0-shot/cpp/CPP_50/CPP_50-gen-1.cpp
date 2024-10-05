Here is the answer:

```cpp
#include<stdio.h>
#include<string>
using namespace std;
string encode_shift(string s){
    string out;
    int i;
    for  (i=0; i<s.length(); i++)
    {
        int w=((int)s[i]+5-(int)'a')%26+(int)'a';
        out=out+(char)w;
    }
    return out;
}
string decode_shift(string s){
    string out;
    int i;
    for  (i=0; i<s.length(); i++)
    {
        int w=((int)s[i]-5-(int)'a')%26+(int)'a';
        out=out+(char)w;
    }
    return out;
}
```

Explanation:

The encode_shift function works by taking the ASCII value of each character in the input string, adding 5 to it, and then using the modulus operator to make sure that the result is a valid ASCII value for a character in the alphabet. The decode_shift function does the same thing, but subtracts 5 instead of adding 5.

So for example, if you have the string "hello", the encode_shift function will return "mjqqt". The decode_shift function will then return "hello".

This is a simple form of encryption known as a Caesar cipher, which is used in many old-fashioned encryption methods.

Note: This code will only work correctly with lower-case letters. If you want to include upper-case letters, you will need to add additional code to handle them.

Also, this code does not handle non-alphabet characters in the input string. If you want to include them, you will need to add additional code to handle them.

Lastly, this code uses the ASCII values of the characters to perform the encryption and decryption. This is a very basic form of encryption and is not secure against modern-day attacks. If you need a secure encryption method, you should use a library that is designed for that.
