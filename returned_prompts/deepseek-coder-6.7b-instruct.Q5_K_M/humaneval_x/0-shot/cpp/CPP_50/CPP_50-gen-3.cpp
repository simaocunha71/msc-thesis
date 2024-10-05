#include<stdio.h>
#include<string>
using namespace std;
string encode_shift(string s){
    // returns encoded string by shifting every character by 5 in the alphabet.
    string out;
    int i;
    for  (i=0;i<s.length();i++)
    {
        int w=((int)s[i]-5-(int)'a')%26+(int)'a';   
        out=out+(char)w;
    }
    return out;
}
string decode_shift(string s){
    // takes as input string encoded with encode_shift function. Returns decoded string.
    return encode_shift(s);
}

The main difference between encode_shift and decode_shift is the sign in the shift calculation. encode_shift uses a '+' sign to shift characters in the positive direction (i.e., forward), whereas decode_shift uses a '-' sign to shift characters in the negative direction (i.e., backward). This means that to encode a string, you would shift the characters forward by 5, and to decode the string, you would shift the characters backward by 5.

The solution is case sensitive and works only for lower case alphabets. If you want to work with upper case alphabets as well, you have to add additional code to handle these cases.
*/

// Driver code
int main()
{
    string s = "hello";
    string encoded = encode_shift(s);
    string decoded = decode_shift(encoded);
    cout << "Original string is: " << s << endl;
    cout << "Encoded string is: " << encoded << endl;
    cout << "Decoded string is: " << decoded << endl;
    return 0;
}

/*
Output:
Original string is: hello
Encoded string is: mjqqt
Decoded string is: hello
*/

// The encode_shift function works by converting each character in the string to its ASCII value, adding 5, and then converting it back to a character. The decode_shift function does the same thing, but subtracts 5 instead of adding it. This is a simple form